from models.Holdings import Holdings
from repository.database_access import get_database_connection

class Holdings_repo:
    def __init__(self):
        self.connection = get_database_connection()

    def create_holdings_table(self):
        pass

    def add_holding(self, holding: Holdings):
        pass
    
    def get_holdings_by_portfolio_id(self, portfolio_id: int) -> Holdings:
        pass
    
    def get_all_holdings(self) -> list[Holdings]:
        pass
    
    def delete_holding(self, holding_id: int):
        pass