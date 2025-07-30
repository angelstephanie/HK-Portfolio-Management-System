from repository.Portfolio_repo import Portfolio_repo

class PortfolioService:
    def __init__(self):
        self.portfolio_repo = Portfolio_repo()

    def get_portfolio_by_id(self, portfolio_id: int):
        return self.portfolio_repo.get_portfolio_by_id(portfolio_id)
    
    def get_all_portfolios(self):
        return self.portfolio_repo.get_all_portfolios()

    def update_portfolio(self, portfolio):
        return self.portfolio_repo.update_portfolio(portfolio)
