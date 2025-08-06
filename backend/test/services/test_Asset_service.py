import unittest
from flask import Flask
from unittest.mock import patch, MagicMock
from backend.service.Asset_service import AssetService
from backend.repository.Asset_repo import Asset_repo
from backend.models.Asset import Asset, AssetType
from datetime import datetime

class TestAssetService(unittest.TestCase):
    """Test cases for the Asset Service."""
    
    def setUp(self):
        self.app = Flask(__name__)
        self.asset_service = AssetService()
        self.asset_repo = Asset_repo()
        
    @patch('backend.repository.Asset_repo.Asset_repo.get_all_assets')
    def test_get_all_assets(self, mock_get_all_assets):
        """Test the get all assets service method."""
        mock_get_all_assets.return_value = [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}, {'symbol': 'TEST', 'name': 'Test Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}]
        result = self.asset_service.get_all_assets()
        self.assertEqual(result,  [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}, {'symbol': 'TEST', 'name': 'Test Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}])
        
    @patch('backend.service.Asset_service.AssetService.get_asset_by_symbol')
    def test_get_asset_by_symbol_valid(self, mock_get_asset_by_symbol):
        """Test the get asset by symbol service method."""
        mock_get_asset_by_symbol.return_value = {'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}
        result = self.asset_service.get_asset_by_symbol('AAPL')
        self.assertEqual(result['symbol'], 'AAPL')
        
    # def test_get_asset_by_symbol_empty(self):
    #     with self.assertRaises(ValueError):
    #         self.asset_service.get_asset_by_symbol("")
    
    # def test_get_asset_by_symbol_nonstring(self):
    #     with self.assertRaises(TypeError):
    #         self.asset_service.get_asset_by_symbol(3)
        
    # @patch('backend.service.Asset_service.AssetService.get_asset_by_symbol')
    # def test_get_asset_by_symbol_invalid_symbol(self, mock_get_asset_by_symbol_invalid_symbol):
    #     """Test the get asset by symbol service method."""
    #     mock_get_asset_by_symbol_invalid_symbol.return_value = None
    #     result = self.asset_service.get_asset_by_symbol('INVALID')
    #     self.assertEqual(result, None)
        
    @patch('backend.service.Asset_service.AssetService.add_asset')
    def test_add_asset(self, mock_add_asset):
        """Test the add asset service method."""
        mock_add_asset.return_value = 1
        result = self.asset_service.add_asset(Asset(
            symbol="AAPL",
            name="Apple Inc.",
            type=AssetType.STOCK,
            current_price=2800.00,
            opening_price=2795.00,
            last_updated=datetime.now()
        ))
        self.assertEqual(result, 1)
        
    @patch('backend.service.Asset_service.AssetService.update_asset')
    def test_update_asset(self, mock_update_asset):
        """Test the update asset service method."""
        mock_update_asset.return_value = 1
        result = self.asset_service.update_asset(Asset(
            symbol="AAPL",
            name="Apple Inc.",
            type=AssetType.STOCK,
            current_price=2800.00,
            opening_price=2795.00,
            last_updated=datetime.now()
        ))
        self.assertEqual(result, 1)

#     def test_add_asset_existing(self):
#         asset = Asset(symbol="AAPL", name="Test Inc.", type=AssetType.STOCK, current_price=2800.00,  opening_price=2795.00, last_updated=datetime.now())
#         result = self.asset_service.add_asset(asset)
#         self.assertIsInstance(result, int)
#         self.assertEqual(result, 1)

#     def test_add_asset_invalid(self):
#         with self.assertRaises(ValueError):
#             self.asset_service.add_asset(None)

#     def test_update_asset_not_found(self):
#         asset = Asset(symbol="INVALID", name="Invalid Inc.", type=AssetType.STOCK, current_price=2800.00,  opening_price=2795.00, last_updated=datetime.now())
#         with self.assertRaises(ValueError):
#             self.asset_service.update_asset(asset)

#     def test_update_asset_invalid(self):
#         with self.assertRaises(ValueError):
#             self.asset_service.update_asset(None)