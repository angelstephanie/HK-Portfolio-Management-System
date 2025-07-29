from models.Asset import Asset, AssetType
from repository.database_access import get_database_connection

class Asset_repo:
    def __init__(self):
        self.connection = get_database_connection()

    def create_asset_table(self):
        """Create the Asset table in the database if it does not exist."""
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT Assets EXITS(
                symbol VARCHAR(20) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                type ENUM('stock', 'crypto', 'etf', 'bond'),
                current_price DECIMAL(15, 2),
                last_updated TIMESTAMP
            );
        """)
        self.connection.commit()
        cursor.close()
    
    def get_asset_by_symbol(self, symbol: str) -> Asset:
        pass
    
    def get_all_assets(self) -> list[Asset]:
        pass
    
    def add_asset(self, asset: Asset):
        pass
    
    def delete_asset(self, symbol: str):
        pass
    
    
    
    
    