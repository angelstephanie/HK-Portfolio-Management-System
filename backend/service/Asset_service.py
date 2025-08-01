from backend.repository.Asset_repo import Asset_repo
from backend.YahooFetcher import YahooFetcher
class AssetService:
    def __init__(self):
        self.asset_repo = Asset_repo()
        self.yahooFetcher = YahooFetcher()
            
    def get_asset_by_symbol(self, symbol: str):
        asset = self.yahooFetcher.get_asset(symbol)
        if asset:
            self.asset_repo.update_asset(asset)
        return self.asset_repo.get_asset_by_symbol(symbol)
    
    def get_all_assets(self):
        assets = self.yahooFetcher.get_all_assets()
        if assets:
            for asset in assets:
                self.asset_repo.update_asset(asset)
                
        return self.asset_repo.get_all_assets()
    
    def add_asset(self, asset):
        asset = self.yahooFetcher.get_asset(asset.symbol)
        if asset:
            self.asset_repo.update_asset(asset)
        return self.asset_repo.add_asset(asset)
    
    def update_asset(self, asset):
        asset = self.yahooFetcher.get_asset(asset.symbol)
        if asset:
            self.asset_repo.update_asset(asset)
            
        return self.asset_repo.update_asset(asset)