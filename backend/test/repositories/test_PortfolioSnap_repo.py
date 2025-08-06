from backend.repository.PortfolioSnap_repo import PortfolioSnap_repo
from backend.models.PortfolioSnap import PortfolioSnap
from datetime import datetime

def setup():
    global portfolio_snap_repo
    portfolio_snap_repo = PortfolioSnap_repo()
    global snapshot_date
    snapshot_date = datetime.strptime("2023-12-02 12:00:00", "%Y-%m-%d %H:%M:%S")
    global new_portfolio_snap
    new_portfolio_snap = PortfolioSnap(
        portfolio_id=1,
        cash_value=10000.00,
        invested_value=1500.00,
        snapshot_date=snapshot_date
    )
    

def test_add_portfolio_snap():
    portfolio_snap_add = portfolio_snap_repo.add_portfolio_snap(new_portfolio_snap)
    
    assert portfolio_snap_add is not None
    assert isinstance(portfolio_snap_add, int)    
    assert portfolio_snap_add == 1
    
def test_get_portfolio_snap_by_id():
    portfolio_id = 1
    portfolio_snap = portfolio_snap_repo.get_portfolio_snap_by_id(portfolio_id,snapshot_date)
    
    assert portfolio_snap is not None
    assert isinstance(portfolio_snap, PortfolioSnap)
    assert portfolio_snap.portfolio_id == portfolio_id
    assert portfolio_snap.cash_value == 10000.00
    assert portfolio_snap.invested_value == 1500.00

def test_get_all_portfolio_snaps():
    portfolio_snaps = portfolio_snap_repo.get_all_portfolio_snaps()
    
    assert isinstance(portfolio_snaps, list)
    assert len(portfolio_snaps) > 0
    
    for snap in portfolio_snaps:
        assert isinstance(snap, PortfolioSnap)
        assert snap.portfolio_id is not None
        assert snap.cash_value is not None
        assert snap.invested_value is not None
        assert snap.snapshot_date is not None

def test_update_portfolio_snap():
    # Update the portfolio snap's cash value
    new_portfolio_snap.cash_value += 500.00
    updated_count = portfolio_snap_repo.update_portfolio_snap(new_portfolio_snap)
    
    assert updated_count is not None
    assert isinstance(updated_count, int)
    assert updated_count == 1
    
    # Verify the update
    portfolio_snap = portfolio_snap_repo.get_portfolio_snap_by_id(new_portfolio_snap.portfolio_id,snapshot_date)
    assert portfolio_snap.cash_value == new_portfolio_snap.cash_value

def test_delete_portfolio_snap():
    portfolio_id = 1
    portfolio_snap = portfolio_snap_repo.get_portfolio_snap_by_id(portfolio_id,snapshot_date)
    
    assert portfolio_snap is not None
    
    deleted_count = portfolio_snap_repo.delete_portfolio_snap(portfolio_id,snapshot_date)
    
    assert deleted_count == 1
    
    # Verify the deletion
    deleted_snap = portfolio_snap_repo.get_portfolio_snap_by_id(portfolio_id,snapshot_date)
    assert deleted_snap is None

def run_tests():
    setup()
    test_add_portfolio_snap()
    test_get_portfolio_snap_by_id()
    test_get_all_portfolio_snaps()
    test_update_portfolio_snap()
    test_delete_portfolio_snap()
    print("All tests in PortfolioSnap repository passed!")