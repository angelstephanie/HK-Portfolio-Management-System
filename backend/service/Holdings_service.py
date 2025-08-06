from backend.repository.Holdings_repo import Holdings_repo  
from backend.models.Holdings import Holdings
from decimal import Decimal
class HoldingsService:
    def __init__(self):
        self.holdings_repo = Holdings_repo()

    def add_holding(self, holding):
        if not holding:
            raise ValueError("Holding cannot be empty")
        if not isinstance(holding, Holdings):
            raise TypeError("Holding must be a Holdings object")
        
        return self.holdings_repo.add_holding(holding)
    
    def get_holdings_by_id(self, portfolio_id: int):
        if not portfolio_id:
            raise ValueError("Portfolio_id cannot be empty")
        if not isinstance(portfolio_id,int):
            raise TypeError("Portfolio_id must be an int")
        
        return self.holdings_repo.get_holdings_by_id(portfolio_id)

    def update_holding(self, holding: Holdings):
        if not holding:
            raise ValueError("Holding cannot be empty")
        if not isinstance(holding, Holdings):
            raise TypeError("Holding must be a Holdings object")
        
        # Calculate the new average buying price
        existing_holding = self.holdings_repo.get_holdings_by_holding_id(holding.holding_id)
        if not existing_holding:
            raise ValueError("Holding does not exist")

        total_quantity = existing_holding.quantity + holding.quantity
        if total_quantity == 0:
            raise ValueError("Total quantity cannot be zero")
        
        holding.avg_buy_price = (
        (Decimal(existing_holding.avg_buy_price) * existing_holding.quantity) +
        (Decimal(holding.avg_buy_price) * holding.quantity)
        ) / total_quantity
        holding.quantity = total_quantity
        
        return self.holdings_repo.update_holding(holding)
    
    def get_all_holdings(self):
        return self.holdings_repo.get_all_holdings()
    
    def delete_holding(self, holding_id: int):
        if not holding_id:
            raise ValueError("Holding_id cannot be empty")
        if not isinstance(holding_id,int):
            raise TypeError("Holding_id must be an int")
        
        return self.holdings_repo.delete_holding(holding_id)