from backend.repository.Holdings_repo import Holdings_repo
from backend.models.Holdings import Holdings
from datetime import datetime

def setup():
    global holdings_repo
    holdings_repo = Holdings_repo()
    global new_holding
    new_holding = Holdings(
        portfolio_id=1,
        symbol="AMZN",
        quantity=10,
        avg_buy_price=215.00
    )

def test_add_holding():
    holdings_add = holdings_repo.add_holding(new_holding)
    
    assert holdings_add is not None
    assert isinstance(holdings_add, int)    
    assert holdings_add == 1

def test_get_holdings_by_id():
    portfolio_id=1
    holdings = holdings_repo.get_holdings_by_id(portfolio_id)
    
    for holding in holdings:
        assert holding is not None
        assert isinstance(holding, Holdings)
        assert holding.portfolio_id == portfolio_id
        assert holding.symbol is not None
        assert holding.quantity is not None
        assert holding.avg_buy_price is not None

def test_get_all_holdings():
    holdings = holdings_repo.get_all_holdings()
    
    assert isinstance(holdings, list)
    assert len(holdings) > 0
    
    for holding in holdings:
        assert isinstance(holding, Holdings)
        assert holding.holding_id is not None
        assert holding.portfolio_id is not None
        assert holding.symbol is not None
        assert holding.quantity is not None
        assert holding.avg_buy_price is not None
        

def test_update_holding():
    # Update the holding's quantity
    new_holding.quantity += 5
    updated_holding = holdings_repo.update_holding(new_holding)
    
    assert updated_holding is not None
    assert isinstance(updated_holding, int)
    assert updated_holding == 1
    
    # Verify the update
    holding = holdings_repo.get_holdings_by_id(new_holding.holding_id)
    assert holding.quantity == 15

def test_delete_holding():
    holding_id = new_holding.holding_id
    deleted_count = holdings_repo.delete_holding(holding_id)
    
    assert deleted_count == 1
    
    # Verify the deletion
    holding = holdings_repo.get_holdings_by_id(holding_id)
    assert holding is None

def run_tests():
    setup()
    test_get_holdings_by_id()
    test_get_all_holdings()
    test_add_holding()
    test_update_holding()
    test_delete_holding()
    print("All tests in Holdings repository passed!")
    

