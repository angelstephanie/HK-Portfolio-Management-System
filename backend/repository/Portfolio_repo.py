from models.Portfolio import Portfolio
from repository.database_access import get_database_connection

class Portfolio_repo:
    def __init__(self):
        self.connection = get_database_connection()

    def create_portfolio_table(self):
        pass

    def add_portfolio(self, portfolio: Portfolio):
        pass

    def get_by_id(self, portfolio_id: int) -> Portfolio:
        pass

    def get_all_portfolios(self) -> list[Portfolio]:
        pass

    def delete_portfolio(self, portfolio_id: int):
        pass