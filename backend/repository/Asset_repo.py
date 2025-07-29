from models.Asset import Asset, AssetType
from repository.database_access import get_database_connection

class Asset_repo:
    def __init__(self):
        self.connection = get_database_connection()

    def create_asset_table(self):
        pass
    
    def get_asset_by_symbol(self, symbol: str) -> Asset:
        pass
    
    def get_all_assets(self) -> list[Asset]:
        pass
    
    def add_asset(self, asset: Asset):
        pass
    
    def delete_asset(self, symbol: str):
        pass
    
    
    
    
    