from backend.models.Watchlist import Watchlist
from backend.models.Asset import Asset, AssetType
from backend.repository.database_access import get_database_connection

class Watchlist_repo:
    def __init__(self):
        self.connection = get_database_connection()
    
    def add_asset2watchlist(self, watchlist_element :Watchlist):
        """Add a new asset symbol to the watchlist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                            INSERT INTO Watchlist (symbol)
                            VALUES (%s)
                            """, (watchlist_element.symbol,))

            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Watchlist updated: {watchlist_element}")
            
            return affected_rows if affected_rows > 0 else None
        
        except Exception as e:
            print(f"❌ Error updating Watchlist: {e}")
            return None
    
    def get_watchlist(self):
        """Retrieve all assets in the watchlist."""
        try:
            cursor = self.connection.cursor()
            self.connection.commit()
            cursor.execute("SELECT * FROM Watchlist LEFT JOIN Assets USING (symbol)")
            rows = cursor.fetchall()
            cursor.close()
            
            assets = []
            for row in rows:
                assets.append(Asset(
                    symbol=row[0],
                    name=row[1],
                    type=AssetType(row[2]),
                    current_price=row[3],
                    opening_price=row[4],
                    last_updated=row[5]
                ))
            print(f"✅ Watchlist retrieved {len(assets)} assets")
            return assets
        except Exception as e:
            print(f"❌ Error retrieving watchlist: {e}")
            return None
    
    def remove_asset_from_watchlist(self, symbol: str):
        """Remove an asset symbol from the watchlist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Watchlist WHERE symbol = %s", (symbol,))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Asset removed from watchlist: {symbol}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error removing asset from watchlist: {e}")
            return None