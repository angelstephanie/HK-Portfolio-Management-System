from datetime import datetime

class Portfolio:
    def __init__(self, portfolio_id: int, name: str, description: str = "", created_at: datetime = None):
        self.portfolio_id = portfolio_id
        self.name = name
        self.description = description
        self.created_at = created_at or datetime.now()
