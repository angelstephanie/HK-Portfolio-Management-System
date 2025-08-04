from backend.models.Holdings import Holdings
from datetime import datetime

def test_creation():
    holding = Holdings(
        id=1,
        asset_symbol="AAPL",
        quantity=10,
        purchase_price=150.00,
        purchase_date=datetime.strptime("2023-10-01"),
        last_updated=datetime.strptime("2023-10-01 12:00:00")
    )
    
    assert holding.id == 1
    assert holding.asset_symbol == "AAPL"
    assert holding.quantity == 10
    assert holding.purchase_price == 150.00
    assert holding.purchase_date == datetime.strptime("2023-10-01")
    assert holding.last_updated == datetime.strptime("2023-10-01 12:00:00")