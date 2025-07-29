from datetime import datetime

class Portfolio:
    def __init__(self, name: str, created_at: datetime, portfolio_id = None, description: str = ""):
        self.__portfolio_id = portfolio_id
        self.__name = name
        self.__description = description
        self.__created_at = created_at

    @property
    def portfolio_id(self):
        return self.__portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        self.__portfolio_id = portfolio_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        if not isinstance(value, datetime):
            raise ValueError("created_at must be a datetime object")
        self.__created_at = value