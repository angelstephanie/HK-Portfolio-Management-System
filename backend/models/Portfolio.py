from datetime import datetime

class Portfolio:
    def __init__(self, name: str, created_at: datetime, portfolio_id = None, description: str = ""):
        self.__portfolio_id = portfolio_id
        self.__name = name
        self.__description = description
        self.__created_at = created_at

    def get_portfolio_id(self):
        return self.__portfolio_id

    def set_portfolio_id(self, portfolio_id):
        self.__portfolio_id = portfolio_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_created_at(self):
        return self.__created_at

    def set_created_at(self, value):
        if not isinstance(value, datetime):
            raise ValueError("created_at must be a datetime object")
        self.__created_at = value