from backend.models.Transaction import Transaction, TransactionType
from datetime import datetime

def test_creation():
    transaction = Transaction(
        transaction_id=1,
        portfolio_id = 1,
        symbol="AAPL",
        type = TransactionType.BUY,
        quantity=10,
        price_per_unit=150.00,
        fee=5.00,
        timestamp=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    )
    
    assert transaction.transaction_id == 1
    assert transaction.portfolio_id == 1
    assert transaction.symbol == "AAPL"
    assert transaction.type == TransactionType.BUY
    assert transaction.quantity == 10
    assert transaction.price_per_unit == 150.00
    assert transaction.fee == 5.00
    assert transaction.timestamp == datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    
def run_tests():
    test_creation()
    print("All tests in testing model Transaction passed!")