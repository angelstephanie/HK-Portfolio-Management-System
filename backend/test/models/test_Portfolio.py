from backend.models.Portfolio import Portfolio
from datetime import datetime

def test_creation():
    portfolio = Portfolio(
        portfolio_id=1,
        name="Tech Portfolio",
        description="A portfolio focused on technology stocks",
        created_at=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    )
    
    assert portfolio.portfolio_id == 1
    assert portfolio.name == "Tech Portfolio"
    assert portfolio.description == "A portfolio focused on technology stocks"
    assert portfolio.created_at == datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")

def run_tests():
    test_creation()
    print("All tests in testing model Portfolio passed!")