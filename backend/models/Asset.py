from datetime import datetime
from enum import Enum

class AssetType(Enum):
    STOCK = 'stock'
    CRYPTO = 'crypto'
    ETF = 'etf'
    BOND = 'bond'
    
class Asset:
    def __init__(self, symbol: str, name: str , type: AssetType, current_price: float, last_updated: datetime):
        self.__symbol = symbol
        self.__name = name
        self.__type = type  # 'stock', 'crypto', 'etf', 'bond'
        self.__current_price = current_price
        self.__last_updated = last_updated or datetime.now()

    
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        self.__symbol = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if not isinstance(value, AssetType):
            raise ValueError("type must be an instance of AssetType")
        self.__type = value

    @property
    def current_price(self):
        return self.__current_price

    @current_price.setter
    def current_price(self, value):
        self.__current_price = value

    @property
    def last_updated(self):
        return self.__last_updated

    @last_updated.setter
    def last_updated(self, value):
        if not isinstance(value, datetime):
            raise ValueError("last_updated must be a datetime object")
        self.__last_updated = value