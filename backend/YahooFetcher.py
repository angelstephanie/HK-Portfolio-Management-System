import yfinance as yf
import pandas as pd
import json
from datetime import datetime
from sqlalchemy import create_engine, text

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
        with open(symbols, "r") as f:
            self.asset_dict = json.load(f)

    
    def fetchByAssetType(self, asset_type: str = None) -> pd.DataFrame:
        """
        Download current pricing information for specific type of asset.
        
        Parameters:
        asset_type (str): Specify one asset type (e.g., 'stock', 'crypto').
                          If None, downloads for all types in self.asset_dict.
        
        Returns:
        pd.DataFrame: A dataframe containing asset information.
        """
        results = []

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


        return pd.DataFrame(results)
    
    def fetchBySymbol(self, symbol: str, asset_type: str) -> dict:
        """
        Download current pricing information for specific symbol of asset.

        Parameters:
        symbol (str): The asset symbol (e.g., 'AAPL', 'BTC-USD')
        asset_type (str): The asset type ('stock', 'crypto', 'etf', 'bond')
        
        Returns:
        pd.DataFrame: A dataframe containing asset information.
        """
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            name = info.get('shortName', 'N/A')
            price = info.get('regularMarketPrice', None)
            now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

            results =  {
                'symbol': symbol,
                'name': name,
                'type': asset_type,
                'current_price': round(price, 2) if price else None,
                'last_updated': now
            }
            return pd.DataFrame([results])

        except Exception as e:
            print(f"[Error] Failed to fetch data for '{symbol}': {e}")
            return pd.DataFrame()
        
        

    def saveTodb(self, df):
        """
        Save the asset DataFrame into the Assets table.

        Parameters:
        - df (pd.DataFrame): The asset information to save
        """
        try:
            # Initialize database engine
            engine = create_engine(f"mysql+pymysql://{self.username}:{self.password}@127.0.0.1:3306/{self.schema}")

            with engine.connect() as conn:
                for _, row in df.iterrows():
                    conn.execute(text("""
                        INSERT INTO Assets (symbol, name, type, current_price, last_updated)
                        VALUES (:symbol, :name, :type, :current_price, :last_updated)
                        ON DUPLICATE KEY UPDATE
                            name = VALUES(name),
                            type = VALUES(type),
                            current_price = VALUES(current_price),
                            last_updated = VALUES(last_updated)
                    """), row.to_dict())
                conn.commit()
            print("✅ Data successfully saved to the Assets table.")
        except Exception as e:
            print(f"❌ Failed to save data: {e}")

    def run(self):
        """
        Fetch current price data from Yahoo and save into asset table.
        """
       # Download all assets across all types listed in asset_info.json
        df_all_assets = self.fetchByAssetType()
        print(df_all_assets.head(10))
        
        # save to database
        self.saveTodb(df_all_assets)

