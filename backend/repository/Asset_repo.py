from backend.models.Asset import Asset, AssetType
from backend.repository.database_access import get_database_connection

class Asset_repo:
    def __init__(self):
        self.connection = get_database_connection()

    def add_asset(self, asset: Asset):
        """Add a new asset to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO Assets (symbol, name, type, current_price, last_updated)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    name = VALUES(name),
                    type = VALUES(type),
                    current_price = VALUES(current_price),
                    opening_price = VALUES(opening_price),
                    last_updated = VALUES(last_updated)
            """, (asset.symbol, asset.name, asset.type.value, asset.current_price, asset.opening_price, asset.last_updated))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Asset added/updated: {asset.symbol}")
        except Exception as e:
            print(f"❌ Error adding/updating asset: {e}")
            
        return affected_rows if affected_rows > 0 else None
    

    def update_asset(self, asset: Asset):
        """Update an existing asset in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Assets
                SET name = %s, type = %s, current_price = %s, opening_price = %s, last_updated = %s
                WHERE symbol = %s
            """, (asset.name, asset.type.value, asset.current_price, asset.opening_price, asset.last_updated, asset.symbol))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Asset updated: {asset.symbol}")
        except Exception as e:
            print(f"❌ Error updating asset: {e}")
        
        return affected_rows if affected_rows > 0 else None
    
     
    def delete_asset(self, symbol: str):
        """Delete an asset by its symbol."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Assets WHERE symbol = %s", (symbol,))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Asset deleted: {symbol}")
        except Exception as e:
            print(f"❌ Error deleting asset: {e}") 
        
        return affected_rows if affected_rows > 0 else None
    

    def get_asset_by_symbol(self, symbol: str) -> Asset:
        """Retrieve an asset by its symbol."""
        # cursor = self.connection.cursor()
        # cursor.execute("SELECT * FROM Assets WHERE symbol = %s", (symbol,))
        # row = cursor.fetchone()
        # cursor.close()
        
        # if row:
        #     return Asset(
        #         symbol=row[0],
        #         name=row[1],
        #         type=AssetType(row[2]),
        #         current_price=row[3],
        #         opening_price=row[4],
        #         last_updated=row[5]
        #     )
        # return None
        import json
        with open('backend/assets_data.json', 'r') as file:
            assets_data = json.load(file)
        for asset in assets_data:
            if asset['symbol'] == symbol:
                return asset

    def get_all_assets(self) -> list[Asset]:
        """Retrieve all assets from the database."""
        # cursor = self.connection.cursor()
        # cursor.execute("SELECT * FROM Assets")
        # rows = cursor.fetchall()
        # cursor.close()
        
        # assets = []
        # for row in rows:
        #     assets.append(Asset(
        #         symbol=row[0],
        #         name=row[1],
        #         type=AssetType(row[2]),
        #         current_price=row[3],
        #         opening_price=row[4],
        #         last_updated=row[5]
        #     ))
        # return assets
        import json 
        with open('backend/assets_data.json', 'r') as file:
            assets_data = json.load(file)
        return assets_data
    

    
    
    
    
    