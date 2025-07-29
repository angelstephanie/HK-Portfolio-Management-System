class Holdings:
    def __init__(self, portfolio_id: int, symbol: str,
                 quantity: float, avg_buy_price: float, holding_id: int = None):
        self.__holding_id = holding_id
        self.__portfolio_id = portfolio_id
        self.__symbol = symbol
        self.__quantity = quantity
        self.__avg_buy_price = avg_buy_price

    
    @property
    def holding_id(self):
        return self.__holding_id

    @holding_id.setter
    def holding_id(self, value):
        self.__holding_id = value

    @property
    def portfolio_id(self):
        return self.__portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, value):
        self.__portfolio_id = value

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        self.__symbol = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def avg_buy_price(self):
        return self.__avg_buy_price

    @avg_buy_price.setter
    def avg_buy_price(self, value):
        self.__avg_buy_price = value