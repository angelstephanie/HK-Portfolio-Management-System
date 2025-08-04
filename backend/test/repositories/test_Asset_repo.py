from backend.repository.Asset_repo import Asset_repo
from backend.models.Asset import Asset
from datetime import datetime


def test_get_asset_by_symbol():
    asset_repo = Asset_repo()
    symbol = "AAPL"
    asset = asset_repo.get_asset_by_symbol(symbol)
    
    assert asset is not None
    assert asset.symbol == symbol
    
    