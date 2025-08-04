from backend.models.Transaction import Transaction
from datetime import datetime

def test_creation():
    transaction = Transaction(
        id=1,
        asset_symbol="AAPL",
        quantity=10,
        price_per_unit=150.00,
        transaction_date=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
        transaction_type="BUY"
    )
    
    assert transaction.id == 1
    assert transaction.asset_symbol == "AAPL"
    assert transaction.quantity == 10
    assert transaction.price_per_unit == 150.00
    assert transaction.transaction_date == datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    assert transaction.transaction_type == "BUY"