import unittest
from flask import Flask
from unittest.mock import patch
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
        """Test the get all assets service method, with correct behavior."""
        mock_get_all_assets.return_value = [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}, {'symbol': 'TEST', 'name': 'Test Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}]
        result = self.asset_service.get_all_assets()
        self.assertEqual(result,  [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}, {'symbol': 'TEST', 'name': 'Test Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}])
    
    @patch('backend.repository.Asset_repo.Asset_repo.get_all_assets')
    def test_get_all_assets_exception(self, mock_get_all_assets):
        """Test the get all assets service method, when get_all_assets from repo layer returns None due to exception."""
        mock_get_all_assets.return_value = None
        result = self.asset_service.get_all_assets()
        self.assertEqual(result, None)
    
    @patch('backend.YahooFetcher.YahooFetcher.fetchByAssetType')    
    def test_get_all_assets_fetch_issue(self, mock_fetchByAssetType):
        """Test the get all assets service method, when fetchByAssetType returns an empty list."""
        mock_fetchByAssetType.return_value = []
        result = self.asset_service.get_all_assets()
        self.assertEqual(result, None)
        
    @patch('backend.repository.Asset_repo.Asset_repo.get_asset_by_symbol')
    def test_get_asset_by_symbol(self, mock_get_asset_by_symbol):
        """Test the get asset by symbol service method, with correct behavior."""
        mock_get_asset_by_symbol.return_value = {'symbol': 'AAPL', 'name': 'Apple Inc.', 'type': 'stock', 'current_price': 150.0, 'opening_price': 145.0, 'last_updated': '2023-10-01'}
        result = self.asset_service.get_asset_by_symbol('AAPL')
        self.assertEqual(result['symbol'], 'AAPL')
        
    def test_get_asset_by_symbol_empty(self):
        """Test the get asset by symbol service method, when symbol is an empty string."""
        with self.assertRaises(ValueError):
            self.asset_service.get_asset_by_symbol("")
    
    def test_get_asset_by_symbol_nonstring(self):
        """Test the get asset by symbol service method, when symbol is not of String type."""
        with self.assertRaises(TypeError):
            self.asset_service.get_asset_by_symbol(3)
        
    def test_get_asset_by_symbol_invalid_symbol(self):
        """Test the get asset by symbol service method, when symbol is invalid."""
        with self.assertRaises(ValueError):
            self.asset_service.get_asset_by_symbol("INVALID")
        
    @patch('backend.repository.Asset_repo.Asset_repo.add_asset')
    def test_add_asset(self, mock_add_asset):
        """Test the add asset service method, with correct behavior."""
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
    
    @patch('backend.repository.Asset_repo.Asset_repo.update_asset')
    @patch('backend.YahooFetcher.YahooFetcher.fetchBySymbol')
    @patch('backend.repository.Asset_repo.Asset_repo.get_asset_by_symbol')
    def test_add_asset_existing(self, mock_get_asset_by_symbol, mock_fetchBySymbol, mock_update_asset ):
        """Test the add asset service method, when asset already exists in our database."""
        mock_update_asset.return_value = 1
        mock_fetchBySymbol.return_value = Asset(
            symbol="AAPL",
            name="Apple Inc.",
            type=AssetType.STOCK,
            current_price=2800.00,
            opening_price=2795.00,
            last_updated="2025-08-06 18:11:05"
        )
        mock_get_asset_by_symbol.return_value = Asset(
            symbol="AAPL",
            name="Apple Inc.",
            type=AssetType.STOCK,
            current_price=2800.00,
            opening_price=2795.00,
            last_updated="2025-08-06 18:11:06"
        )
        
        result = self.asset_service.add_asset(Asset(
            symbol="AAPL",
            name="Apple Inc.",
            type=AssetType.STOCK,
            current_price=2800.00,
            opening_price=2795.00,
            last_updated=datetime.now()
        ))
        
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_add_asset_none(self):
        """Test the add asset service method, when asset is None."""
        with self.assertRaises(ValueError):
            self.asset_service.add_asset(None)
    
    def test_add_asset_non_asset(self):
        """Test the add asset service method, when asset is not of Asset type."""
        with self.assertRaises(TypeError):
            self.asset_service.add_asset(3)
        
    @patch('backend.service.Asset_service.AssetService.update_asset')
    def test_update_asset(self, mock_update_asset):
        """Test the update asset service method, with correct behavior."""
        mock_update_asset.return_value = 1
        result = self.asset_service.update_asset(Asset(
            symbol="AAPL",
            name="Apple Inc.",
            type=AssetType.STOCK,
            current_price=2800.00,
            opening_price=2795.00,
            last_updated=datetime.now()
        ))
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_update_asset_none(self):
        """Test the update asset service method, when asset is None."""
        with self.assertRaises(ValueError):
            self.asset_service.update_asset(None)
    
    def test_update_asset_non_asset(self):
        """Test the update asset service method, when asset is not of Asset type."""
        with self.assertRaises(TypeError):
            self.asset_service.update_asset(3)
    
    def test_update_asset_not_found(self):
        """Test the update asset service method, when fetchBySymbol raises a value error due to an invalid symbol."""
        asset = Asset(symbol="INVALID", name="Invalid Inc.", type=AssetType.STOCK, current_price=2800.00,  opening_price=2795.00, last_updated=datetime.now())
        with self.assertRaises(ValueError):
            self.asset_service.update_asset(asset)
    
    @patch('backend.YahooFetcher.YahooFetcher.fetchBySymbol')    
    def test_update_asset_fetch_issue(self, mock_fetchBySymbol):
        """Test the update asset service method, when fetchBySymbol returns an empty list due to exception."""
        mock_fetchBySymbol.return_value = []
        result = self.asset_service.update_asset(Asset(
            symbol="AAPL",
            name="Apple Inc.",
            type=AssetType.STOCK,
            current_price=2800.00,
            opening_price=2795.00,
            last_updated=datetime.now()
        ))
        self.assertEqual(result, None)
            
    @patch('backend.service.Asset_service.AssetService.get_price_by_range')
    def test_get_price_by_range(self, mock_get_price_by_range):
        """Test the get price by range service method, with correct behavior."""
        mock_get_price_by_range.return_value = {'2023-01-03': 123.47061920166016, '2023-01-04': 124.74411010742188, '2023-01-05': 123.4212646484375, '2023-01-06': 127.96244049072266}
        result = self.asset_service.get_price_by_range('AAPL', 1)
        self.assertEqual(result, {'2023-01-03': 123.47061920166016, '2023-01-04': 124.74411010742188, '2023-01-05': 123.4212646484375, '2023-01-06': 127.96244049072266})
    
    def test_get_price_range_empty_symbol(self):
        """Test the get price by range service method, when symbol is an empty string."""
        with self.assertRaises(ValueError):
            self.asset_service.get_price_by_range("", "2025-08-07")
            
    def test_get_price_range_non_string_symbol(self):
        """Test the get price by range service method, when symbol is not of String type."""
        with self.assertRaises(TypeError):
            self.asset_service.get_price_by_range(2, "2025-08-07")
            
    def test_get_price_range_empty_date(self):
        """Test the get price by range service method, when start_date is an empty string."""
        with self.assertRaises(ValueError):
            self.asset_service.get_price_by_range("AAPL", "")
    
    @patch('backend.service.Asset_service.AssetService.get_price_within_day')
    def test_get_price_within_day(self, mock_get_price_within_day):
        """Test the get price within day service method, with correct behavior."""
        mock_get_price_within_day.return_value = {'2025-08-06 09:30:00': 209.54, '2025-08-06 10:00:00': 210.76, '2025-08-06 10:30:00': 211.07, '2025-08-06 11:00:00': 214.23, '2025-08-06 11:30:00': 214.63, '2025-08-06 12:00:00': 214.5, '2025-08-06 12:30:00': 214.48, '2025-08-06 13:00:00': 214.54, '2025-08-06 13:30:00': 214.38, '2025-08-06 14:00:00': 214.6, '2025-08-06 14:30:00': 214.4, '2025-08-06 15:00:00': 213.88, '2025-08-06 15:30:00': 213.25}
        result = self.asset_service.get_price_within_day('AAPL', 1)
        self.assertEqual(result, {'2025-08-06 09:30:00': 209.54, '2025-08-06 10:00:00': 210.76, '2025-08-06 10:30:00': 211.07, '2025-08-06 11:00:00': 214.23, '2025-08-06 11:30:00': 214.63, '2025-08-06 12:00:00': 214.5, '2025-08-06 12:30:00': 214.48, '2025-08-06 13:00:00': 214.54, '2025-08-06 13:30:00': 214.38, '2025-08-06 14:00:00': 214.6, '2025-08-06 14:30:00': 214.4, '2025-08-06 15:00:00': 213.88, '2025-08-06 15:30:00': 213.25})
    
    def test_get_price_range_empty_symbol(self):
        """Test the get price within day service method, when symbol is an empty string."""
        with self.assertRaises(ValueError):
            self.asset_service.get_price_within_day("", 1)
            
    def test_get_price_range_non_string_symbol(self):
        """Test the get price within day service method, when symbol is not of String type."""
        with self.assertRaises(TypeError):
            self.asset_service.get_price_within_day(2, 1)
            
    def test_get_price_range_empty_date(self):
        """Test the get price within day service method, when period is <= 0"""
        with self.assertRaises(ValueError):
            self.asset_service.get_price_within_day("AAPL", 0)