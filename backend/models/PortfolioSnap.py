from datetime import datetime

class PortfolioSnap:
    def __init__(self, portfolio_id: int, snapshot_date: datetime, cash_value: float, invested_value: float):
        self.__portfolio_id = portfolio_id
        self.__snapshot_date = snapshot_date
        self.__cash_value = cash_value
        self.__invested_value = invested_value
        
    @property
    def portfolio_id(self):
        return self.__portfolio_id
    
    @portfolio_id.setter
    def portfolio_id(self, value):
        self.__portfolio_id = value
        
    @property
    def snapshot_date(self):
        return self.__snapshot_date
    
    @snapshot_date.setter
    def snapshot_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("snapshot_date must be a datetime object")
        self.__snapshot_date = value
    
    @property
    def cash_value(self):
        return self.__cash_value

    @cash_value.setter
    def cash_value(self, value):
        self.__cash_value = value
        
    @property
    def invested_value(self):
        return self.__invested_value
    
    @invested_value.setter
    def invested_value(self, value):
        self.__invested_value = value
        
    def __str__(self):
        return f"PortfolioSnap(portfolio_id={self.portfolio_id}, snapshot_date={self.snapshot_date}, " \
               f"cash_value={self.cash_value}, invested_value={self.invested_value})"
    
    def to_dict(self):
        """Convert the portfolio snapshot to a dictionary."""
        return {
            "portfolio_id": self.portfolio_id,
            "snapshot_date": self.snapshot_date,
            "cash_value": self.cash_value,
            "invested_value": self.invested_value
        }