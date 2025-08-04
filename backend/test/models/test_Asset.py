from backend.models.Asset import Asset, AssetType
from datetime import datetime
import unittest


def test_creation():
    asset = Asset(
        symbol="AAPL",
        name="Apple Inc.",
        type=AssetType.STOCK,
        current_price=150.00,
        opening_price=148.00,
        last_updated=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    )
    
    assert asset.symbol == "AAPL"
    assert asset.name == "Apple Inc."
    assert asset.type == AssetType.STOCK
    assert asset.current_price == 150.00
    assert asset.opening_price == 148.00
    assert asset.last_updated == datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")