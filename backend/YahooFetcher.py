import yfinance as yf
import pandas as pd
import json
from datetime import datetime
from backend.models.Asset import Asset, AssetType
from pytz import timezone
from tzlocal import get_localzone 

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
    
    def fetchPriceByRange(self, symbol:str, start: str, end: str):
        """
        Download historical pricing information for a specific symbol of asset within a date range.

        Parameters:
        symbol (str): The asset symbol (e.g., 'AAPL', 'BTC-USD')
        start (str): Start date in 'YYYY-MM-DD' format
        end (str): End date in 'YYYY-MM-DD' format
        
        Returns:
        dict: A dictionary with dates as keys and closing prices as values.
        """
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(start=start, end=end)
            df.reset_index(inplace=True)
            df.drop(columns=['Open', 'High', 'Low', 'Volume','Dividends', 'Stock Splits'], inplace=True, errors='ignore')
            df['Close'] = df['Close'].round(2)
            df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
            df = df.set_index('Date')['Close'].to_dict()
            print(f"✅ Retrieved historical prices for {symbol} from {start} to {end}")
            return df
        except Exception as e:
            print(f"[Error] Failed to fetch historical data for '{symbol}': {e}")
            return None
    
    def fetchPriceWithinDay(self, symbol: str, period: int):
        """
        Download day time intraday pricing information for a specific symbol of asset.

        Parameters:
        symbol (str): The asset symbol (e.g., 'AAPL', 'BTC-USD')
        
        Returns:
        dict: A dictionary with datetime as keys and closing prices as values.
        """
        try:
            ny_tz = timezone('US/Eastern')
            print("local_tz",ny_tz)
            df = yf.download(tickers = symbol, period= str(period) + "d", interval='30m',auto_adjust=True)
            df.reset_index(inplace=True)
            df.drop(columns=['Open', 'High', 'Low', 'Volume'], inplace=True, errors='ignore')
            df['Close'] = df['Close'].round(2)
            df['Datetime'] = df['Datetime'].dt.tz_convert(ny_tz)

            df['Datetime'] = df['Datetime'].dt.strftime("%Y-%m-%d %H:%M:%S")
            df = df.set_index('Datetime')['Close'].to_dict()
            
            print(f"✅ Retrieved intraday prices for {symbol} for the last {period} days")
            return df[symbol]
        except Exception as e:
            print(f"[Error] Failed to fetch intraday data for '{symbol}': {e}")
            return None

if __name__ == "__main__":
    # Example usage
    fetcher = YahooFetcher()
    df = fetcher.fetchPriceWithinDay("AAPL" ,1)
    # df = fetcher.fetchPriceByRange("MSFT", "2023-01-01", "2023-10-01")
    print(df)