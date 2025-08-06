import unittest
from flask import Flask, jsonify
from unittest.mock import patch, MagicMock
from backend.controller.Asset_controller import asset_controller
from backend.service.Asset_service import AssetService

class TestAssetController(unittest.TestCase):
    """Test cases for the Asset Controller."""
    
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(asset_controller)
        self.asset_service = AssetService()
        
    @patch('backend.service.Asset_service.AssetService.get_all_assets')
    def test_get_all_assets(self, mock_get_all_assets):
        """Test the get all assets endpoint."""
        mock_get_all_assets.return_value = [MagicMock(to_dict=lambda: {'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'})]
        response = self.app.test_client().get('/assets')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        
    @patch('backend.service.Asset_service.AssetService.get_asset_by_symbol')
    def test_get_asset_by_symbol(self, mock_get_asset_by_symbol):
        """Test the get asset by symbol endpoint."""
        mock_get_asset_by_symbol.return_value = MagicMock(to_dict=lambda: {'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'})
        response = self.app.test_client().get('/assets/AAPL')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['symbol'], 'AAPL')
        
    @patch('backend.service.Asset_service.AssetService.add_asset')
    def test_add_asset(self, mock_add_asset):
        """Test the add asset endpoint."""
        mock_add_asset.return_value = 1
        response = self.app.test_client().post('/assets', json={'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Asset added successfully')
        
    @patch('backend.service.Asset_service.AssetService.update_asset')
    def test_update_asset(self, mock_update_asset):
        """Test the update asset endpoint."""
        mock_update_asset.return_value = 1
        response = self.app.test_client().put('/assets/AAPL', json={'name': 'Apple Inc.', 'type': 'stock', 'current_price': 155.0, 'opening_price': 150.0, 'last_updated': '2023-10-01'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Asset updated successfully')
        
    @patch('backend.service.Asset_service.AssetService.get_price_by_range')
    def test_get_price_by_range(self, mock_get_price_by_range):
        """Test the get closing price endpoint"""
        mock_get_price_by_range.return_value = {'2023-01-03': 123.47061920166016, '2023-01-04': 124.74411010742188, '2023-01-05': 123.4212646484375, '2023-01-06': 127.96244049072266}
        response = self.app.test_client().get('/assets/AAPL/historicprice/2023-01-03')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'2023-01-03': 123.47061920166016, '2023-01-04': 124.74411010742188, '2023-01-05': 123.4212646484375, '2023-01-06': 127.96244049072266})
    
    @patch('backend.service.Asset_service.AssetService.get_price_within_day')
    def test_get_price_within_day(self, mock_get_price_within_day):
        """Test the get closing price endpoint"""
        mock_get_price_within_day.return_value = {'2025-08-05 09:30:00': 203.37, '2025-08-05 10:00:00': 204.53, '2025-08-05 10:30:00': 204.23, '2025-08-05 11:00:00': 204.63, '2025-08-05 11:30:00': 203.92, '2025-08-05 12:00:00': 203.71, '2025-08-05 12:30:00': 203.85, '2025-08-05 13:00:00': 204.04, '2025-08-05 13:30:00': 204.03, '2025-08-05 14:00:00': 203.87, '2025-08-05 14:30:00': 203.58, '2025-08-05 15:00:00': 203.34, '2025-08-05 15:30:00': 202.93}
        response = self.app.test_client().get('/assets/AAPL/historicprice/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'2025-08-05 09:30:00': 203.37, '2025-08-05 10:00:00': 204.53, '2025-08-05 10:30:00': 204.23, '2025-08-05 11:00:00': 204.63, '2025-08-05 11:30:00': 203.92, '2025-08-05 12:00:00': 203.71, '2025-08-05 12:30:00': 203.85, '2025-08-05 13:00:00': 204.04, '2025-08-05 13:30:00': 204.03, '2025-08-05 14:00:00': 203.87, '2025-08-05 14:30:00': 203.58, '2025-08-05 15:00:00': 203.34, '2025-08-05 15:30:00': 202.93})

    # def run_tests(self):
    #     unittest.TextTestRunner().run(unittest.makeSuite(self.__class__))
    #     print("All asset controller tests pass")
    
# def run_unittest():
#     unittest.TextTestRunner().run(unittest.makeSuite(TestAssetController))
#     print("All asset controller tests pass")