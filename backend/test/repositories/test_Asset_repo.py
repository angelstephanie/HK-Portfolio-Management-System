from backend.repository.Asset_repo import Asset_repo
from backend.models.Asset import Asset, AssetType
from datetime import datetime
import math

def setup():
    global asset_repo
    asset_repo = Asset_repo()
    global new_asset
    new_asset = Asset(
        symbol="GOOGL",
        name="Alphabet Inc.",
        type=AssetType.STOCK,
        current_price=2800.00,
        opening_price=2795.00,
        last_updated=datetime.now()
    )

def test_add_asset():
    assets_add = asset_repo.add_asset(new_asset)
    
    assert assets_add is not None
    assert isinstance(assets_add, int)    
    assert assets_add == 1
    
def test_get_asset_by_symbol():
    symbol = "AAPL"
    asset = asset_repo.get_asset_by_symbol(symbol)
    
    assert asset is not None
    assert isinstance(asset, Asset)
    assert asset.symbol == symbol
    assert asset.name == "Apple Inc."
    assert asset.type == AssetType.STOCK
    assert math.isclose(asset.current_price, 202.38, rel_tol=1e-9)
    assert math.isclose(asset.opening_price, 211.00, rel_tol=1e-9)
    assert asset.last_updated == datetime.strptime("2025-08-04 07:36:03", "%Y-%m-%d %H:%M:%S")

def test_get_all_assets():
    assets = asset_repo.get_all_assets()
    
    assert isinstance(assets, list)
    assert len(assets) > 0
    
    for asset in assets:
        assert isinstance(asset, Asset)
        assert asset.symbol is not None
        assert asset.name is not None
        assert asset.type is not None
        assert asset.current_price is not None
        assert asset.opening_price is not None
        assert asset.last_updated is not None

def test_update_asset():
    # Update the asset's current price
    new_price = 2100.00
    new_asset.current_price = new_price
    
    updated_count = asset_repo.update_asset(new_asset)
    
    assert updated_count == 1
    
    # Verify the update
    updated_asset = asset_repo.get_asset_by_symbol(new_asset.symbol)
    assert updated_asset.current_price == new_price
    
def test_delete_asset():
    symbol = "GOOGL"
    asset = asset_repo.get_asset_by_symbol(symbol)
    
    assert asset is not None
    
    deleted_count = asset_repo.delete_asset(symbol)
    
    assert deleted_count == 1
    
    # Verify the deletion
    deleted_asset = asset_repo.get_asset_by_symbol(symbol)
    assert deleted_asset is None

def run_tests():
    setup()
    test_get_asset_by_symbol()
    test_get_all_assets()
    test_add_asset()
    test_update_asset()
    test_delete_asset()
    print("All tests in Asset repository passed!")
