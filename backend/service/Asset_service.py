from backend.repository.Asset_repo import Asset_repo
from backend.YahooFetcher import YahooFetcher
from backend.models.Asset import Asset
class AssetService:
    def __init__(self):
        self.asset_repo = Asset_repo()
        self.yahooFetcher = YahooFetcher()
            
    def get_asset_by_symbol(self, symbol: str):
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        if not isinstance(symbol, str):
            raise TypeError("Symbol must be a string")
        
        asset = self.yahooFetcher.fetchBySymbol(symbol)
        if asset:
            self.asset_repo.update_asset(asset)
        return self.asset_repo.get_asset_by_symbol(symbol)
    
    def get_all_assets(self):
        assets = self.yahooFetcher.fetchByAssetType()
        if assets:
            for asset in assets:
                self.asset_repo.update_asset(asset)
                
        return self.asset_repo.get_all_assets()
    
    def add_asset(self, asset):
        if not asset:
            raise ValueError("Asset cannot be empty")
        if not isinstance(asset, Asset):
            raise TypeError("Asset must be an Asset")
        
        asset = self.yahooFetcher.fetchBySymbol(asset.symbol)
        if asset:
            self.asset_repo.update_asset(asset)
        return self.asset_repo.add_asset(asset)
    
    def update_asset(self, asset):
        if not asset:
            raise ValueError("Asset cannot be empty")
        if not isinstance(asset, Asset):
            raise TypeError("Asset must be a object of Asset")
        
        asset = self.yahooFetcher.fetchBySymbol(asset.symbol)
        if asset:
            self.asset_repo.update_asset(asset)
            
        return self.asset_repo.update_asset(asset)