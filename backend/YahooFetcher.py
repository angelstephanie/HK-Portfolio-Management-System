import yfinance as yf
import pandas as pd
import json
from datetime import datetime

class YahooFetcher:
    def __init__(self, symbols: list[str], start_date: str, end_date: str):        
        """
        symbols: list of stock symbols (e.g., ['GOOG', 'AAPL'])
        start_date: string format 'YYYY-MM-DD'
        end_date: string format 'YYYY-MM-DD'
        """
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date
        with open("asset_info.json", "r") as f:
            self.asset_dict = json.load(f)

        self.dataframes = {}
    
    def fetchByAssetType(self, asset_type: str = None) -> pd.DataFrame:
        """
        Download current information for given asset type or all types.
        
        Parameters:
        asset_type (str): Optional; specify one asset type (e.g., 'stock', 'crypto').
                          If None, downloads for all types in self.asset_dict.
        
        Returns:
        pd.DataFrame: A dataframe containing symbol, name, type, current_price, and last_updated.
        """
        results = []

        # Decide which asset types to fetch
        types_to_download = [asset_type] if asset_type else list(self.asset_dict.keys())

        for asset in types_to_download:
            for symbol in self.asset_dict.get(asset, []):
                try:
                    ticker = yf.Ticker(symbol)
                    info = ticker.info

                    name = info.get('shortName', 'N/A')
                    price = info.get('regularMarketPrice', None)
                    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

                    results.append({
                        'symbol': symbol,
                        'name': name,
                        'type': asset,
                        'current_price': round(price, 2) if price else None,
                        'last_updated': now
                    })

                except Exception as e:
                    print(f"[Error] Failed to process symbol '{symbol}': {e}")
                    continue

        # Convert the list of dictionaries into a DataFrame
        return pd.DataFrame(results)
    
    def fetchBYSymbol(self, symbol: str) -> dict:
        """
        Fetch current price and info for a single symbol.

        Parameters:
        symbol (str): The symbol to fetch data for (e.g., 'AAPL', 'BTC-USD')

        Returns:
        dict: A dictionary with symbol, name, type, current_price, and last_updated
        """
        asset_type = None
        for atype, symbols in self.asset_dict.items():
            if symbol in symbols:
                asset_type = atype
                break

        if asset_type is None:
            print(f"[Warning] Symbol '{symbol}' not found in asset_info.json.")
            asset_type = "unknown"

        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            name = info.get('shortName', 'N/A')
            price = info.get('regularMarketPrice', None)
            now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

            return {
                'symbol': symbol,
                'name': name,
                'type': asset_type,
                'current_price': round(price, 2) if price else None,
                'last_updated': now
            }

        except Exception as e:
            print(f"[Error] Failed to fetch data for '{symbol}': {e}")
            return {}
        
    def saveTodb(self,df):
        pass

    

if __name__ == "__main__":
    # Initialize the fetcher with empty symbol list, since asset types are in asset_info.json
    fetcher = YahooFetcher([], '2023-01-01', '2023-12-31')

    # Download all assets across all types listed in asset_info.json
    df_all_assets = fetcher.fetchByAssetType()

    # Display first few rows
    print(df_all_assets.head(10))

