class Watchlist:
    def __init__(self, symbol: str):
        self.__symbol = symbol

    @property
    def symbol(self):
        return self.__symbol
    
    @symbol.setter
    def symbol(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Symbol must be a string")
        self.__symbol = value

    def __str__(self):
        return f"Watchlist(symbol={self.symbol})"
    
    def to_dict(self):
        return {"symbol": self.symbol}