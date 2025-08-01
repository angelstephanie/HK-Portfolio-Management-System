import yfinance as yf
import pandas as pd
import json
from datetime import datetime
from backend.models.Asset import Asset, AssetType

class YahooFetcher:
    def __init__(self):                
        with open('asset_info.json', "r") as f:
            self.asset_dict = json.load(f)

    
    def fetchByAssetType(self, asset_type: str = None):
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
                    current_price = info.get('regularMarketPrice', None)
                    opening_price = info.get('regularMarketOpen', None)
                    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    results_asset = Asset(symbol=symbol,name=name, 
                                          type=AssetType(asset), 
                                          current_price=round(current_price, 2) if current_price else None, 
                                          opening_price=round(opening_price) if opening_price else None, 
                                          last_updated=now)
                    result_assets.append(results_asset)

                except Exception as e:
                    print(f"[Error] Failed to process symbol '{symbol}': {e}")
                    continue


        return result_assets
    
    def fetchBySymbol(self, symbol: str):
        """
        Download current pricing information for specific symbol of asset.

        Parameters:
        symbol (str): The asset symbol (e.g., 'AAPL', 'BTC-USD')
        asset_type (str): The asset type ('stock', 'crypto', 'etf', 'bond')
        
        Returns:
        Asset: An Asset object containing the fetched data.
        """
        asset_type = None
        for type in self.asset_dict.keys():
            if symbol in self.asset_dict[type]:
                asset_type = type
                break
        if not asset_type:
            raise ValueError(f"Symbol '{symbol}' not found in asset_info.json")
        
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            name = info.get('shortName', 'N/A')
            current_price = info.get('regularMarketPrice', None)
            opening_price = info.get('regularMarketOpen', None)
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            results_asset = Asset(symbol=symbol,name=name, 
                                          type=AssetType(asset_type), 
                                          current_price=round(current_price, 2) if current_price else None, 
                                          opening_price=round(opening_price) if opening_price else None, 
                                          last_updated=now)
            return results_asset

        except Exception as e:
            print(f"[Error] Failed to fetch data for '{symbol}': {e}")
            return None
    
    # import json
    # from datetime import datetime

    # def fetchByAssetType_test(self, asset_type: str = None) -> list:
    #     """
    #     Download current pricing information for a specific type of asset,
    #     including the opening price, and store the data into a JSON file.

    #     Parameters:
    #     asset_type (str): Specify one asset type (e.g., 'stock', 'crypto').
    #                     If None, downloads for all types in self.asset_dict.

    #     Returns:
    #     list[Asset]: A list of Asset objects containing the fetched data.
    #     """
    #     result_assets = []
    #     assets_json_data = []

    #     types_to_download = [asset_type] if asset_type else list(self.asset_dict.keys())

    #     for asset in types_to_download:
    #         for symbol in self.asset_dict.get(asset, []):
    #             try:
    #                 ticker = yf.Ticker(symbol)
    #                 info = ticker.info

    #                 name = info.get('shortName', 'N/A')
    #                 current_price = info.get('regularMarketPrice', None)
    #                 opening_price = info.get('regularMarketOpen', None)
    #                 now = datetime.now()

    #                 # results_asset = Asset(
    #                 #     symbol=symbol,
    #                 #     name=name,
    #                 #     type=AssetType(asset),
    #                 #     current_price=round(current_price, 2) if current_price else None,
    #                 #     opening_price=round(opening_price, 2) if opening_price else None,
    #                 #     last_updated=now
    #                 # )
    #                 # result_assets.append(results_asset)

    #                 # Prepare data for JSON serialization
    #                 asset_json = {
    #                     "symbol": symbol,
    #                     "name": name,
    #                     "type": asset,
    #                     "opening_price": round(opening_price, 2) if opening_price else None,
    #                     "current_price": round(current_price, 2) if current_price else None,
    #                     "last_updated": now.isoformat()
    #                 }
    #                 assets_json_data.append(asset_json)

    #             except Exception as e:
    #                 print(f"[Error] Failed to process symbol '{symbol}': {e}")
    #                 continue

    #     # Save to JSON file
    #     try:
    #         with open("assets_data.json", "w") as json_file:
    #             json.dump(assets_json_data, json_file, indent=4)
    #         print("[Info] Asset data saved to 'assets_data.json'")
    #     except Exception as e:
    #         print(f"[Error] Failed to write JSON file: {e}")

    #     return result_assets

    
    #     ## just for testing purpose
    # def saveTodb(self, asserts):
        
    #     asserts_repo = Asset_repo()
    #     try:
    #         for asset in asserts:
    #             asserts_repo.add_asset(asset)
    #         print("✅ All assets saved to the database successfully.")
    #     except Exception as e:
    #         print(f"❌ Failed to save assets to the database: {e}")
        
    #     print(asserts_repo.get_asset_by_symbol('AAPL'))
            

#     def run(self):
#         """
#         Fetch current price data from Yahoo and save into asset table.
#         """
#        # Download all assets across all types listed in asset_info.json
#         df_all_assets = self.fetchByAssetType_test()
#         print(df_all_assets)
        
#         # # # save to database
#         # self.saveTodb(df_all_assets)

# if __name__ == "__main__":
#     # Example usage
#     fetcher = YahooFetcher(symbols='asset_info.json', username='root', password='n3u3da!', schema='HongKongHackathon')
#     fetcher.run()