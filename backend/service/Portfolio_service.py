from backend.repository.Portfolio_repo import Portfolio_repo
from backend.models.Portfolio import Portfolio
class PortfolioService:
    def __init__(self):
        self.portfolio_repo = Portfolio_repo()

    def get_portfolio_by_id(self, portfolio_id: int):
        if not portfolio_id:
            raise ValueError("portfolio_id cannot be empty")
        if not isinstance(portfolio_id, int):
            raise TypeError("portfolio_id must be an int")
        
        return self.portfolio_repo.get_portfolio_by_id(portfolio_id)
    
    def get_all_portfolios(self):
        return self.portfolio_repo.get_all_portfolios()

    def update_portfolio(self, portfolio):
        if not portfolio:
            raise ValueError("portfolio cannot be empty")
        if not isinstance(portfolio, Portfolio):
            raise TypeError("portfolio must be a object of Portfolio")
        
        return self.portfolio_repo.update_portfolio(portfolio)
