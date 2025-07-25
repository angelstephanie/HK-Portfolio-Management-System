class Holdings:
    def __init__(self, holding_id: int, portfolio_id: int, symbol: str,
                 quantity: float, avg_buy_price: float):
        self.holding_id = holding_id
        self.portfolio_id = portfolio_id
        self.symbol = symbol
        self.quantity = quantity
        self.avg_buy_price = avg_buy_price
