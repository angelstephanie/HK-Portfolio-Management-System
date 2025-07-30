import yfinance as yf
import pandas as pd
import json
from datetime import datetime
from models.Asset import Asset, AssetType
from repository.Asset_repo import Asset_repo

class YahooFetcher:
    def __init__(self, symbols: str, username: str, password: str, schema: str):        
        """
        symbols: json file name
        username: MySQL username (e.g., 'root')
        password: MySQL password
        schema: MySQL schema/database name (e.g., 'HongKongHackathon')
        """
        self.username = username
        self.password = password
        self.schema = schema
        with open('asset_info.json', "r") as f:
            self.asset_dict = json.load(f)

    
    def fetchByAssetType(self, asset_type: str = None) -> pd.DataFrame:
        """
        Download current pricing information for specific type of asset.
        
        Parameters:
        asset_type (str): Specify one asset type (e.g., 'stock', 'crypto').
                          If None, downloads for all types in self.asset_dict.
        
        Returns:
        list[Asset]: A list of Asset objects containing the fetched data.
        """
        result_assets = []

        types_to_download = [asset_type] if asset_type else list(self.asset_dict.keys())

        for asset in types_to_download:
            for symbol in self.asset_dict.get(asset, []):
                try:
                    ticker = yf.Ticker(symbol)
                    info = ticker.info

                    name = info.get('shortName', 'N/A')
                    price = info.get('regularMarketPrice', None)
                    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                    results_asset = Asset(symbol=symbol,name=name, type=AssetType(asset), current_price=round(price, 2) if price else None, last_updated=now)
                    result_assets.append(results_asset)

                except Exception as e:
                    print(f"[Error] Failed to process symbol '{symbol}': {e}")
                    continue


        return result_assets
    
    def fetchBySymbol(self, symbol: str, asset_type: str) -> dict:
        """
        Download current pricing information for specific symbol of asset.

        Parameters:
        symbol (str): The asset symbol (e.g., 'AAPL', 'BTC-USD')
        asset_type (str): The asset type ('stock', 'crypto', 'etf', 'bond')
        
        Returns:
        Asset: An Asset object containing the fetched data.
        """
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            name = info.get('shortName', 'N/A')
            price = info.get('regularMarketPrice', None)
            now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

            results_asset = Asset(symbol=symbol,name=name, type=AssetType(asset_type), current_price=round(price, 2) if price else None, last_updated=now)
            return results_asset

        except Exception as e:
            print(f"[Error] Failed to fetch data for '{symbol}': {e}")
            return None
        
    
        ## just for testing purpose
    def saveTodb(self, asserts):
        
        asserts_repo = Asset_repo()
        try:
            for asset in asserts:
                asserts_repo.add_asset(asset)
            print("✅ All assets saved to the database successfully.")
        except Exception as e:
            print(f"❌ Failed to save assets to the database: {e}")
        
        print(asserts_repo.get_asset_by_symbol('AAPL'))
            

    def run(self):
        """
        Fetch current price data from Yahoo and save into asset table.
        """
       # Download all assets across all types listed in asset_info.json
        df_all_assets = self.fetchByAssetType()
        print(df_all_assets)
        
        # # save to database
        self.saveTodb(df_all_assets)

if __name__ == "__main__":
    # Example usage
    fetcher = YahooFetcher(symbols='asset_info.json', username='root', password='n3u3da!', schema='HongKongHackathon')
    fetcher.run()