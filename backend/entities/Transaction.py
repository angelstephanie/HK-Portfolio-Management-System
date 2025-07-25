from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    BUY = 'buy'
    SELL = 'sell'
    
    
class Transaction:
    def __init__(self, transaction_id: int, portfolio_id: int, symbol: str,
                 type: TransactionType, quantity: float, price_per_unit: float, fee: float = 0.0,
                 timestamp: datetime = None, notes: str = ""):
        self.transaction_id = transaction_id
        self.portfolio_id = portfolio_id
        self.symbol = symbol
        self.type = type  # 'buy' or 'sell'
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.fee = fee
        self.timestamp = timestamp or datetime.now()
        self.notes = notes
