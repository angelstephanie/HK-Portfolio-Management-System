from backend.repository.PortfolioSnap_repo import PortfolioSnap_repo
from datetime import datetime
from backend.models.PortfolioSnap import PortfolioSnap

class PortfolioSnapService:
    def __init__(self):
        self.portfolio_snap_repo = PortfolioSnap_repo()

    def add_portfolio_snap(self, portfolio_snap):
        if not portfolio_snap:
            raise ValueError("portfolio_snap cannot be empty")
        if not isinstance(PortfolioSnap,portfolio_snap):
            raise TypeError("portfolio must be a object of Portfolio")
        
        return self.portfolio_snap_repo.add_portfolio_snap(portfolio_snap)
        
    def update_portfolio_snap(self, portfolio_snap):
        if not portfolio_snap:
            raise ValueError("portfolio_snap cannot be empty")
        if not isinstance(PortfolioSnap,portfolio_snap):
            raise TypeError("portfolio must be a object of Portfolio")
        
        return self.portfolio_snap_repo.update_portfolio_snap(portfolio_snap)

    def get_portfolio_snap_by_id(self, snap_id: int, snap_date: datetime):
        if not snap_id or not snap_date:
            raise ValueError("snap_id or snap_date cannot be empty")
        if not isinstance(datetime,snap_date) or not isinstance(snap_id,int):
            raise TypeError("snap_date must be a datetime object and snap_id must be an int")
        
        return self.portfolio_snap_repo.get_portfolio_snap_by_id(snap_id,snap_date)

    def get_all_portfolio_snaps(self):
        return self.portfolio_snap_repo.get_all_portfolio_snaps()
