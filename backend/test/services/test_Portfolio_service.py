import unittest
from flask import Flask
from unittest.mock import patch
from backend.service.Portfolio_service import PortfolioService
from backend.repository.Portfolio_repo import Portfolio_repo
from backend.models.Portfolio import Portfolio
from datetime import datetime

class TestPortfolioService(unittest.TestCase):
    """Test cases for the Portfolio Service."""
    
    def setUp(self):
        self.app = Flask(__name__)
        self.portfolio_service = PortfolioService()
        self.portfolio_repo = Portfolio_repo()
        global new_portfolio
        new_portfolio = Portfolio(
            portfolio_id=1,
            name="Test Portfolio",
            description="A portfolio made for testing",
            created_at=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
        )
        
    @patch('backend.repository.Portfolio_repo.Portfolio_repo.get_all_portfolios')
    def test_get_all_portfolios(self, mock_get_all_portfolios):
        """Test the get all portfolios service method, with correct behavior."""
        mock_get_all_portfolios.return_value = [new_portfolio]
        result = self.portfolio_service.get_all_portfolios()
        self.assertEqual(result, [new_portfolio])
        assert isinstance(result, list)
        assert len(result) > 0
    
        for portfolio in result:
            assert isinstance(portfolio, Portfolio)
            self.assertEqual(portfolio.portfolio_id, 1)
            self.assertEqual(portfolio.name, "Test Portfolio")
            self.assertEqual(portfolio.description, "A portfolio made for testing")
            
    @patch('backend.repository.Portfolio_repo.Portfolio_repo.get_all_portfolios')
    def test_get_all_portfolios_none(self, mock_get_all_portfolios):
        """Test the get all portfolios service method, when get_all_portfolios repo method returns None due to exception."""
        mock_get_all_portfolios.return_value = None
        result = self.portfolio_service.get_all_portfolios()
        self.assertEqual(result, None)
        
    @patch('backend.repository.Portfolio_repo.Portfolio_repo.get_all_portfolios')
    def test_get_all_portfolios_fetch_issue(self, mock_get_all_portfolios):
        """Test the get all portfolios service method, when get_all_portfolios repo method returns [] due to database select issue."""
        mock_get_all_portfolios.return_value = None
        result = self.portfolio_service.get_all_portfolios()
        self.assertEqual(result, None)
            
    @patch('backend.repository.Portfolio_repo.Portfolio_repo.get_portfolio_by_id')
    def test_get_portfolio_by_id(self, mock_get_portfolio_by_id):
        """Test the get portfolio by ID service method."""
        mock_get_portfolio_by_id.return_value = new_portfolio
        result = self.portfolio_service.get_portfolio_by_id(1)
        self.assertEqual(result, new_portfolio)
        assert isinstance(result, Portfolio)
        self.assertEqual(result.portfolio_id, 1)
        self.assertEqual(result.name, "Test Portfolio")
        self.assertEqual(result.description, "A portfolio made for testing")
        
    @patch('backend.repository.Portfolio_repo.Portfolio_repo.get_portfolio_by_id')
    def test_get_portfolio_by_id_none(self, mock_get_portfolio_by_id):
        """Test the get portfolio by ID service method, when get_portfolio_by_id returns None either due to exception or database select issue."""
        mock_get_portfolio_by_id.return_value = None
        result = self.portfolio_service.get_portfolio_by_id(1)
        self.assertEqual(result, None)
        
    def test_get_portfolio_by_id_empty(self):
        """Test the get portfolio by id service method, when portfolio_id is not passed."""
        with self.assertRaises(TypeError):
            self.portfolio_service.get_portfolio_by_id()
            
    def test_get_portfolio_by_id_none_parameter(self):
        """Test the get portfolio by id service method, when portfolio_id is None."""
        with self.assertRaises(ValueError):
            self.portfolio_service.get_portfolio_by_id(None)
            
    def test_get_portfolio_by_id_non_int(self):
        """Test the get portfolio by id service method, when portfolio_id is not of Int type."""
        with self.assertRaises(TypeError):
            self.portfolio_service.get_portfolio_by_id("1")

    @patch('backend.repository.Portfolio_repo.Portfolio_repo.update_portfolio')
    def test_update_portfolio(self, mock_update_portfolio):
        """Test the update portfolio service method, with correct behavior."""
        mock_update_portfolio.return_value = 1
        result = self.portfolio_service.update_portfolio(new_portfolio)
        assert isinstance(result, int)
        self.assertEqual(result, 1)
        
    @patch('backend.repository.Portfolio_repo.Portfolio_repo.update_portfolio')
    def test_update_portfolio_none(self, mock_update_portfolio):
        """Test the update portfolio service method, when update_portfolio repo method returns None either due to exception or database update issue."""
        mock_update_portfolio.return_value = None
        result = self.portfolio_service.update_portfolio(new_portfolio)
        self.assertEqual(result, None)
        
    def test_update_portfolio_empty(self):
        """Test the update portfolio service method, when portfolio is not passed."""
        with self.assertRaises(TypeError):
            self.portfolio_service.update_portfolio()
            
    def test_update_portfolio_none_parameter(self):
        """Test the update portfolio service method, when portfolio is None."""
        with self.assertRaises(ValueError):
            self.portfolio_service.update_portfolio(None)
            
    def test_update_portfolio_non_portfolio(self):
        """Test the update portfolio service method, when portfolio is not of Porfolio type."""
        with self.assertRaises(TypeError):
            self.portfolio_service.update_portfolio("1")