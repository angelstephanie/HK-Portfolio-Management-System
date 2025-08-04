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
        mock_add_asset.return_value = MagicMock(to_dict=lambda: {'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'})
        response = self.app.test_client().post('/assets', json={'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['symbol'], 'AAPL')
        
    @patch('backend.service.Asset_service.AssetService.update_asset')
    def test_update_asset(self, mock_update_asset):
        """Test the update asset endpoint."""
        mock_update_asset.return_value = {'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 155.0, 'opening_price': 150.0, 'last_updated': '2023-10-01'}
        response = self.app.test_client().put('/assets/AAPL', json={'name': 'Apple Inc.', 'type': 'stock', 'current_price': 155.0, 'opening_price': 150.0, 'last_updated': '2023-10-01'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['symbol'], 'AAPL')