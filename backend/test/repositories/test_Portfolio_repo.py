from backend.repository.Portfolio_repo import Portfolio_repo
from backend.models.Portfolio import Portfolio
from datetime import datetime

def setup():
    global portfolio_repo
    portfolio_repo = Portfolio_repo()
    global new_portfolio
    new_portfolio = Portfolio(
        portfolio_id=2,
        name="Tech Portfolio",
        description="A portfolio focused on technology stocks",
        created_at=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    )

def test_add_portfolio():
    portfolio_add = portfolio_repo.add_portfolio(new_portfolio)
    
    assert portfolio_add is not None
    assert isinstance(portfolio_add, int)    
    assert portfolio_add == 1

def test_get_portfolio_by_id():
    portfolio_id = 1
    portfolio = portfolio_repo.get_portfolio_by_id(portfolio_id)
    
    assert portfolio is not None
    assert isinstance(portfolio, Portfolio)
    assert portfolio.portfolio_id == portfolio_id
    assert portfolio.name == "Default"
    assert portfolio.description == "This is the default portfolio"

def test_get_all_portfolios():
    portfolios = portfolio_repo.get_all_portfolios()
    
    assert isinstance(portfolios, list)
    assert len(portfolios) > 0
    
    for portfolio in portfolios:
        assert isinstance(portfolio, Portfolio)
        assert portfolio.portfolio_id is not None
        assert portfolio.name is not None
        assert portfolio.description is not None
        assert portfolio.created_at is not None
    

def test_update_portfolio():
    # Update the portfolio's name
    new_portfolio.name = "Updated Tech Portfolio"
    
    updated_count = portfolio_repo.update_portfolio(new_portfolio)
    
    assert updated_count is not None
    assert isinstance(updated_count, int)
    assert updated_count == 1
    
    # Verify the update
    portfolio = portfolio_repo.get_portfolio_by_id(new_portfolio.portfolio_id)
    assert portfolio.name == "Updated Tech Portfolio"

def test_delete_portfolio():
    portfolio_id = new_portfolio.portfolio_id
    portfolio = portfolio_repo.get_portfolio_by_id(portfolio_id)
    
    assert portfolio is not None
    
    deleted_count = portfolio_repo.delete_portfolio(portfolio_id)
    
    assert deleted_count == 1
    
    # Verify the deletion
    deleted_portfolio = portfolio_repo.get_portfolio_by_id(portfolio_id)
    assert deleted_portfolio is None

def run_tests():
    setup()
    test_get_portfolio_by_id()
    test_get_all_portfolios()
    test_add_portfolio()
    test_update_portfolio()
    test_delete_portfolio()
    print("All tests in Portfolio repository passed!")