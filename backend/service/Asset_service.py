from backend.repository.Asset_repo import Asset_repo
from backend.YahooFetcher import YahooFetcher
from backend.models.Asset import Asset
from backend.repository.Watchlist_repo import Watchlist_repo
from datetime import datetime
class AssetService:
    def __init__(self):
        self.asset_repo = Asset_repo()
        self.watchlist_repo = Watchlist_repo()
        self.yahooFetcher = YahooFetcher()
            
    def get_asset_by_symbol(self, symbol: str):
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        if not isinstance(symbol, str):
            raise TypeError("Symbol must be a string")
        
        asset = self.yahooFetcher.fetchBySymbol(symbol)
        if asset:
            self.asset_repo.update_asset(asset)
            print("✅ Successfully update the lastest asset data.")
            return self.asset_repo.get_asset_by_symbol(symbol)
        else:
            print("❌ No asset found.")
            return None
    
    def get_all_assets(self):
        assets = self.yahooFetcher.fetchByAssetType()
        if assets:
            for asset in assets:
                self.asset_repo.update_asset(asset)
            print("✅ Successfully update the lastest asset data.")
            return self.asset_repo.get_all_assets()
        else:
            print("❌ No assets found.")
            return None
    
    def add_asset(self, asset):
        if not asset:
            raise ValueError("Asset cannot be empty")
        if not isinstance(asset, Asset):
            raise TypeError("Asset must be an Asset")
        
        asset = self.yahooFetcher.fetchBySymbol(asset.symbol)
        if asset:
            check_asset = self.asset_repo.get_asset_by_symbol(asset.symbol)
            if check_asset is None:
                self.watchlist_repo.add_asset2watchlist(asset.symbol)
                return self.asset_repo.add_asset(asset)
            else:
                return self.asset_repo.update_asset(asset)
        else:
            print("❌ No assets found.")
            return None
    
    def update_asset(self, asset):
        if not asset:
            raise ValueError("Asset cannot be empty")
        if not isinstance(asset, Asset):
            raise TypeError("Asset must be a object of Asset")
        
        asset = self.yahooFetcher.fetchBySymbol(asset.symbol)
        if asset:
            check_asset = self.asset_repo.get_asset_by_symbol(asset.symbol)
            if check_asset is None:
                raise ValueError("No asset found in your account, please add the asset first.")
            else:
                return self.asset_repo.update_asset(asset) 
        else:
            print("❌ No assets found.")
            return None
    
    def get_price_by_range(self, symbol: str, start_date: str, end_date = datetime.now().strftime('%Y-%m-%d')):
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        if not isinstance(symbol, str):
            raise TypeError("Symbol must be a string")
        if not start_date or not end_date:
            raise ValueError("Start date and end date cannot be empty")
        
        return self.yahooFetcher.fetchPriceByRange(symbol, start_date, end_date)
    
    def get_price_within_day(self, symbol: str, period: int):
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        if not isinstance(symbol, str):
            raise TypeError("Symbol must be a string")
        if int(period) <= 0:
            raise ValueError("Period must be a positive integer")
        
        return self.yahooFetcher.fetchPriceWithinDay(symbol, period)