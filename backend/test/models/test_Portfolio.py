from backend.models.Portfolio import Portfolio
from datetime import datetime

def test_creation():
    portfolio = Portfolio(
        id=1,
        name="Tech Portfolio",
        description="A portfolio focused on technology stocks",
        creation_date=datetime.strptime("2023-10-01", "%Y-%m-%d"),
        last_updated=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    )
    
    assert portfolio.id == 1
    assert portfolio.name == "Tech Portfolio"
    assert portfolio.description == "A portfolio focused on technology stocks"
    assert portfolio.creation_date == datetime.strptime("2023-10-01", "%Y-%m-%d")
    assert portfolio.last_updated == datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")

def run_tests():
    test_creation()
    print("All tests in testing model Asset passed!")