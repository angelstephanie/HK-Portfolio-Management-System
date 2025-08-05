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
        """Test the get all portfolios service method."""
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

    @patch('backend.repository.Portfolio_repo.Portfolio_repo.update_portfolio')
    def test_update_portfolio(self, mock_update_portfolio):
        """Test the update portfolio service method."""
        mock_update_portfolio.return_value = 1

        result = self.portfolio_service.update_portfolio(new_portfolio)
        assert isinstance(result, int)
        self.assertEqual(result, 1)