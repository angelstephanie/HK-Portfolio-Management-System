from backend.repository.Watchlist_repo import Watchlist_repo

class WatchlistService:
    def __init__(self):
        self.watchlist_repo = Watchlist_repo()
    
    def add_asset_to_watchlist(self, symbol: str):
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        if not isinstance(symbol, str):
            raise TypeError("Symbol must be a string")
        
        return self.watchlist_repo.add_asset2watchlist(symbol)
    
    def get_watchlist(self):
        return self.watchlist_repo.get_watchlist()
    
    def remove_asset_from_watchlist(self, symbol: str):
        if not symbol:
            raise ValueError("Symbol cannot be empty")
        if not isinstance(symbol, str):
            raise TypeError("Symbol must be a string")
        
        return self.watchlist_repo.remove_asset_from_watchlist(symbol)