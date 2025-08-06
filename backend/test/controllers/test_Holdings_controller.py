import unittest
from flask import Flask
from unittest.mock import patch, MagicMock
from backend.controller.Holdings_controller import holdings_controller
from backend.service.Holdings_service import HoldingsService

class TestHoldingsController(unittest.TestCase):
    """Test cases for the Holdings Controller."""
    
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(holdings_controller)
        self.holdings_service = HoldingsService()
        
    @patch('backend.service.Holdings_service.HoldingsService.get_all_holdings')
    def test_get_all_holdings(self, mock_get_all_holdings):
        """Test the get all holdings endpoint."""
        mock_get_all_holdings.return_value = [MagicMock(to_dict=lambda: {'holding_id': 1, 'portfolio_id': 1, 'symbol': 'AAPL', 'quantity': 10, 'avg_buy_price': 150.0})]
        response = self.app.test_client().get('/holdings')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        
    @patch('backend.service.Holdings_service.HoldingsService.get_holdings_by_id')
    def test_get_holdings_by_id(self, mock_get_holdings_by_id):
        """Test the get holdings by portfolio ID endpoint."""
        mock_get_holdings_by_id.return_value = MagicMock(to_dict=lambda: {'holding_id': 1, 'portfolio_id': 1, 'symbol': 'AAPL', 'quantity': 10, 'avg_buy_price': 150.0})
        response = self.app.test_client().get('/holdings/1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(all(holding['portfolio_id'] == 1 for holding in response.json))
        
    @patch('backend.service.Holdings_service.HoldingsService.add_holding')
    def test_add_holding(self, mock_add_holding):
        """Test the add holding endpoint."""
        mock_add_holding.return_value = 1
        response = self.app.test_client().post('/holdings', json={'holding_id': 1, 'portfolio_id': 1, 'symbol': 'AAPL', 'quantity': 10, 'avg_buy_price': 150.0})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Holding added successfully')
        
    @patch('backend.service.Holdings_service.HoldingsService.delete_holding')
    def test_delete_holding(self, mock_delete_holding):
        """Test the delete holding endpoint."""
        mock_delete_holding.return_value = 1
        response = self.app.test_client().delete('/holdings/1')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['message'], 'Holding deleted successfully')
        
    @patch('backend.service.Holdings_service.HoldingsService.update_holding')
    def test_update_holding(self, mock_update_holding):
        """Test the delete holding endpoint."""
        mock_update_holding.return_value = 1
        response = self.app.test_client().put('/holdings', json={'holding_id': 1, 'portfolio_id': 1, 'symbol': 'AAPL', 'quantity': 10, 'avg_buy_price': 150.0})
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['message'], 'Holding updated successfully')