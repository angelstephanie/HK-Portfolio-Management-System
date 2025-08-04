from backend.models.Holdings import Holdings

def test_creation():
    holding = Holdings(
        holding_id=1,
        portfolio_id=1,
        symbol="AAPL",
        quantity=10,
        avg_buy_price=150.00
    )
    
    assert holding.holding_id == 1
    assert holding.portfolio_id == 1
    assert holding.symbol == "AAPL"
    assert holding.quantity == 10
    assert holding.avg_buy_price == 150.00
    
def run_tests():
    test_creation()
    print("All tests in testing model Holdings passed!")