from repository.Holdings_repo import Holdings_repo  

class HoldingsService:
    def __init__(self):
        self.holdings_repo = Holdings_repo()

    def add_holding(self, holding):
        self.holdings_repo.add_holding(holding)
    
    def get_holdings_by_portfolio_id(self, portfolio_id: int):
        return self.holdings_repo.get_holdings_by_portfolio_id(portfolio_id)
    
    def get_all_holdings(self):
        return self.holdings_repo.get_all_holdings()
    
    def delete_holding(self, holding_id: int):
        self.holdings_repo.delete_holding(holding_id)