from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    BUY = 'buy'
    SELL = 'sell'
    
    
class Transaction:
    def __init__(self, portfolio_id: int, symbol: str,
                 type: TransactionType, quantity: float, price_per_unit: float, transaction_id: int = None, fee: float = 0.0,
                 timestamp: datetime = None, notes: str = ""):
        self.__transaction_id = transaction_id
        self.__portfolio_id = portfolio_id
        self.__symbol = symbol
        self.__type = type  # 'buy' or 'sell'
        self.__quantity = quantity
        self.__price_per_unit = price_per_unit
        self.__fee = fee
        self.__timestamp = timestamp or datetime.now()
        self.__notes = notes
    
    # Getter and Setter for transaction_id
    @property
    def transaction_id(self):
        return self.__transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self.__transaction_id = value

    # Getter and Setter for portfolio_id
    @property
    def portfolio_id(self):
        return self.__portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, value):
        self.__portfolio_id = value

    # Getter and Setter for symbol
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        self.__symbol = value

    # Getter and Setter for type
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        print("A")
        if not isinstance(value, TransactionType):
            raise ValueError("type must be an instance of TransactionType Enum")
        self.__type = value

    # Getter and Setter for quantity
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    # Getter and Setter for price_per_unit
    @property
    def price_per_unit(self):
        return self.__price_per_unit

    @price_per_unit.setter
    def price_per_unit(self, value):
        self.__price_per_unit = value

    # Getter and Setter for fee
    @property
    def fee(self):
        return self.__fee

    @fee.setter
    def fee(self, value):
        self.__fee = value

    # Getter and Setter for timestamp
    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        print("B")
        if not isinstance(value, datetime):
            raise ValueError("timestamp must be a datetime object")
        self.__timestamp = value

    # Getter and Setter for notes
    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value
    
    def __str__(self):
        return (f"Transaction(transaction_id={self.transaction_id}, portfolio_id={self.portfolio_id}, "
                f"symbol={self.symbol}, type={self.type.value}, quantity={self.quantity}, "
                f"price_per_unit={self.price_per_unit}, fee={self.fee}, timestamp={self.timestamp}, "
                f"notes='{self.notes}')")
    
    def to_dict(self):
        """Convert the transaction to a dictionary."""
        print("C")
        return {
            "transaction_id": self.transaction_id,
            "portfolio_id": self.portfolio_id,
            "symbol": self.symbol,
            "type": self.type.value,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit,
            "fee": self.fee,
            "timestamp": self.timestamp.isoformat() if isinstance(self.timestamp, datetime) else self.timestamp,
            "notes": self.notes
        }
