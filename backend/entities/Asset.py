from datetime import datetime
from enum import Enum

class AssetType(Enum):
    STOCK = 'stock'
    CRYPTO = 'crypto'
    ETF = 'etf'
    BOND = 'bond'
    
class Asset:
    def __init__(self, symbol: str, name: str, type: AssetType, current_price: float, last_updated: datetime = None):
        self.symbol = symbol
        self.name = name
        self.type = type  # 'stock', 'crypto', 'etf', 'bond'
        self.current_price = current_price
        self.last_updated = last_updated or datetime.now()
