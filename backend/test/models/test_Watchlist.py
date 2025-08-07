from backend.models.Watchlist import Watchlist

def test_create_watchlist():
    """Test creating a new watchlist."""
    watchlist = Watchlist(symbol="AAPL")
    
    assert watchlist is not None
    assert isinstance(watchlist, Watchlist)
    assert watchlist.symbol == "AAPL"

def run_tests():
    """Run all watchlist tests."""
    test_create_watchlist()
    print("Watchlist tests passed successfully!")