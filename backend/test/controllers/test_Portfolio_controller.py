import unittest
from flask import Flask
from unittest.mock import patch, MagicMock
from backend.controller.Portfolio_controller import portfolio_controller
from backend.service.Portfolio_service import PortfolioService

class TestPortfolioController(unittest.TestCase):
    """Test cases for the Portfolio Controller."""
    
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(portfolio_controller)
        self.portfolio_service = PortfolioService()
        
    @patch('backend.service.Portfolio_service.PortfolioService.get_all_portfolios')
    def test_get_all_portfolios(self, mock_get_all_portfolios):
        """Test the get all portfolios endpoint."""
        mock_get_all_portfolios.return_value = [MagicMock(to_dict=lambda: {'id': 1, 'name': 'Test Portfolio', 'description': 'A sample portfolio', 'created_at': '2023-10-01T00:00:00'})]
        response = self.app.test_client().get('/portfolios')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertEqual(response.json[0]['name'], 'Test Portfolio')
        self.assertEqual(response.json[0]['description'], 'A sample portfolio')
        self.assertEqual(response.json[0]['created_at'], '2023-10-01T00:00:00')
        self.assertEqual(response.json[0]['id'], 1)
        
    @patch('backend.service.Portfolio_service.PortfolioService.get_all_portfolios')
    def test_get_all_portfolios_none(self, mock_get_all_portfolios):
        """Test the get all portfolios endpoint."""
        mock_get_all_portfolios.return_value = None
        response = self.app.test_client().get('/portfolios')
        self.assertEqual(response.status_code, 500)
        
    @patch('backend.service.Portfolio_service.PortfolioService.get_portfolio_by_id')
    def test_get_portfolio_by_id(self, mock_get_portfolio_by_id):
        """Test the get portfolio by ID endpoint."""
        mock_get_portfolio_by_id.return_value = MagicMock(to_dict=lambda: {'id': 1, 'name': 'Test Portfolio', 'description': 'A sample portfolio', 'created_at': '2023-10-01T00:00:00'})
        response = self.app.test_client().get('/portfolios/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)
        
    @patch('backend.service.Portfolio_service.PortfolioService.get_portfolio_by_id')
    def test_get_portfolio_by_id_none(self, mock_get_portfolio_by_id):
        """Test the get portfolio by id endpoint."""
        mock_get_portfolio_by_id.return_value = None
        response = self.app.test_client().get('/portfolios/1')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Portfolio not found')
    
    @patch('backend.service.Portfolio_service.PortfolioService.get_portfolio_by_id')
    def test_get_portfolio_by_id_exception(self, mock_get_portfolio_by_id):
        """Test the get portfolio by id endpoint."""
        mock_get_portfolio_by_id.side_effect = Exception('Mocked exception')
        response = self.app.test_client().get('/portfolios/1')
        self.assertEqual(response.status_code, 500)
        
    @patch('backend.service.Portfolio_service.PortfolioService.update_portfolio')
    def test_update_portfolio(self, mock_update_portfolio):
        """Test the update portfolio endpoint."""
        mock_update_portfolio.return_value = 1
        response = self.app.test_client().put('/portfolios/1', json={'id': 1, 'name': 'Updated Portfolio', 'description': 'An updated sample portfolio', 'created_at': '2023-10-01T00:00:00'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Portfolio updated successfully')
        
    @patch('backend.service.Portfolio_service.PortfolioService.update_portfolio')
    def test_update_portfolio_none(self, mock_update_portfolio):
        """Test the update portfolio endpoint."""
        mock_update_portfolio.return_value = None
        response = self.app.test_client().put('/portfolios/1', json={'id': 1, 'name': 'Updated Portfolio', 'description': 'An updated sample portfolio', 'created_at': '2023-10-01T00:00:00'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Portfolio not found')
        
    @patch('backend.service.Portfolio_service.PortfolioService.update_portfolio')
    def test_update_portfolio_exception(self, mock_update_portfolio):
        """Test the update portfolio endpoint."""
        mock_update_portfolio.side_effect = Exception('Mocked exception')
        response = self.app.test_client().put('/portfolios/1', json={'id': 1, 'name': 'Updated Portfolio', 'description': 'An updated sample portfolio', 'created_at': '2023-10-01T00:00:00'})
        self.assertEqual(response.status_code, 500)