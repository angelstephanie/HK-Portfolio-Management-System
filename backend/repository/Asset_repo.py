from models.Asset import Asset, AssetType
from repository.database_access import get_database_connection

class Asset_repo:
    def __init__(self):
        self.connection = get_database_connection()

    def create_asset_table(self):
        """Create the Asset table in the database if it does not exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT Assets EXISTS(
                    symbol VARCHAR(20) PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    type ENUM('stock', 'crypto', 'etf', 'bond'),
                    current_price DECIMAL(15, 2),
                    last_updated TIMESTAMP
                );
            """)
            self.connection.commit()
            cursor.close()
            print("✅ Asset table created successfully.")
        except Exception as e:
            print(f"❌ Error creating Asset table: {e}")
    
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
                    last_updated = VALUES(last_updated)
            """, (asset.symbol, asset.name, asset.type.value, asset.current_price, asset.last_updated))
            self.connection.commit()
            cursor.close()
            print(f"✅ Asset added/updated: {asset.symbol}")
        except Exception as e:
            print(f"❌ Error adding/updating asset: {e}")
    
    def update_asset(self, asset: Asset):
        """Update an existing asset in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Assets
                SET name = %s, type = %s, current_price = %s, last_updated = %s
                WHERE symbol = %s
            """, (asset.name, asset.type.value, asset.current_price, asset.last_updated, asset.symbol))
            self.connection.commit()
            cursor.close()
            print(f"✅ Asset updated: {asset.symbol}")
        except Exception as e:
            print(f"❌ Error updating asset: {e}")
            
    def delete_asset(self, symbol: str):
        """Delete an asset by its symbol."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Assets WHERE symbol = %s", (symbol,))
            self.connection.commit()
            cursor.close()
            print(f"✅ Asset deleted: {symbol}")
        except Exception as e:
            print(f"❌ Error deleting asset: {e}") 
        
    def get_asset_by_symbol(self, symbol: str) -> Asset:
        """Retrieve an asset by its symbol."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Assets WHERE symbol = %s", (symbol,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return Asset(
                symbol=row[0],
                name=row[1],
                type=AssetType(row[2]),
                current_price=row[3],
                last_updated=row[4]
            )
        return None
    
    def get_all_assets(self) -> list[Asset]:
        """Retrieve all assets from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Assets")
        rows = cursor.fetchall()
        cursor.close()
        
        assets = []
        for row in rows:
            assets.append(Asset(
                symbol=row[0],
                name=row[1],
                type=AssetType(row[2]),
                current_price=row[3],
                last_updated=row[4]
            ))
        return assets
    

    
    
    
    
    