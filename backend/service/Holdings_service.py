from backend.repository.Holdings_repo import Holdings_repo  
from backend.models.Holdings import Holdings
class HoldingsService:
    def __init__(self):
        self.holdings_repo = Holdings_repo()

    def add_holding(self, holding):
        if not holding:
            raise ValueError("Holding cannot be empty")
        if not isinstance(holding, Holdings):
            raise TypeError("Holding must be a Holdings object")
        
        return self.holdings_repo.add_holding(holding)
    
    def get_holdings_by_id(self, holding_id: int):
        if not holding_id:
            raise ValueError("Holding_id cannot be empty")
        if not isinstance(holding_id,int):
            raise TypeError("Holding_id must be an int")
        
        return self.holdings_repo.get_holdings_by_id(holding_id)
    
    def get_all_holdings(self):
        return self.holdings_repo.get_all_holdings()
    
    def delete_holding(self, holding_id: int):
        if not holding_id:
            raise ValueError("Holding_id cannot be empty")
        if not isinstance(holding_id,int):
            raise TypeError("Holding_id must be an int")
        
        return self.holdings_repo.delete_holding(holding_id)