from backend.models.PortfolioSnap import PortfolioSnap
from datetime import datetime

def test_creation():
    portfolio_snap = PortfolioSnap(
        portfolio_id=1,
        snapshot_date=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
        cash_value=2000.00,
        invested_value=1500.00
    )
    
    assert portfolio_snap.portfolio_id == 1
    assert portfolio_snap.snapshot_date == datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    assert portfolio_snap.cash_value == 2000.00
    assert portfolio_snap.invested_value == 1500.00

def run_tests():
    test_creation()
    print("All tests in testing model Portfolio passed!")