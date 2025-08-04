from backend.models.PortfolioSnap import PortfolioSnap
from datetime import datetime

def test_creation():
    portfolio_snap = PortfolioSnap(
        id=1,
        portfolio_id=1,
        asset_symbol="AAPL",
        quantity=10,
        total_value=1500.00,
        snapshot_date=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    )
    
    assert portfolio_snap.id == 1
    assert portfolio_snap.portfolio_id == 1
    assert portfolio_snap.asset_symbol == "AAPL"
    assert portfolio_snap.quantity == 10
    assert portfolio_snap.total_value == 1500.00
    assert portfolio_snap.snapshot_date == datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")