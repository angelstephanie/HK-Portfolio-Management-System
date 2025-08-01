from backend.repository.PortfolioSnap_repo import PortfolioSnap_repo
from datetime import datetime

class PortfolioSnapService:
    def __init__(self):
        self.portfolio_snap_repo = PortfolioSnap_repo()

    def add_portfolio_snap(self, portfolio_snap):
        self.portfolio_snap_repo.add_portfolio_snap(portfolio_snap)
        
    def update_portfolio_snap(self, portfolio_snap):
        return self.portfolio_snap_repo.update_portfolio_snap(portfolio_snap)

    def get_portfolio_snap_by_id(self, snap_id: int, snap_date: datetime):
        return self.portfolio_snap_repo.get_portfolio_snap_by_id(snap_id,snap_date)

    def get_all_portfolio_snaps(self):
        return self.portfolio_snap_repo.get_all_portfolio_snaps()
