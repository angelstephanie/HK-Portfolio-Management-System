from backend.repository.Asset_repo import Asset_repo

class AssetService:
    def __init__(self):
        self.asset_repo = Asset_repo()
    
    def get_asset_by_symbol(self, symbol: str):
        return self.asset_repo.get_asset_by_symbol(symbol)
    
    def get_all_assets(self):
        return self.asset_repo.get_all_assets()
    
    def add_asset(self, asset):
        return self.asset_repo.add_asset(asset)
    
    def update_asset(self, asset):
        return self.asset_repo.update_asset(asset)