import unittest
from flask import Flask
from unittest.mock import patch, MagicMock
from backend.service.Holdings_service import HoldingsService
from backend.repository.Holdings_repo import Holdings_repo
from backend.models.Holdings import Holdings

class TestHoldingsService(unittest.TestCase):
    """Test cases for the Asset Service."""
    
    def setUp(self):
        self.app = Flask(__name__)
        self.holdings_service = HoldingsService()
        self.holdings_repo = Holdings_repo()
        global new_holding
        new_holding = Holdings(
            holding_id=1,
            portfolio_id=1,
            symbol="AMZN",
            quantity=10,
            avg_buy_price=215.00
        )
        
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_all_holdings')
    def test_get_all_holdings(self, mock_get_all_holdings):
        """Test the get all assets service method."""
        mock_get_all_holdings.return_value = [new_holding]
        result = self.holdings_service.get_all_holdings()
        self.assertEqual(result, [new_holding])
        assert isinstance(result, list)
        assert len(result) > 0
    
        for holding in result:
            assert isinstance(holding, Holdings)
            self.assertEqual(holding.holding_id, 1)
            self.assertEqual(holding.portfolio_id, 1)
            self.assertEqual(holding.symbol, "AMZN")
            self.assertEqual(holding.quantity, 10)
            self.assertEqual(holding.avg_buy_price, 215.00)
            
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_id')
    def test_get_holding_by_id(self, mock_get_holdings_by_id):
        """Test the get all assets service method."""
        mock_get_holdings_by_id.return_value = [new_holding]
        result = self.holdings_service.get_holdings_by_id(1)
        self.assertEqual(result, [new_holding])
        assert isinstance(result, list)
        assert len(result) > 0
    
        for holding in result:
            assert isinstance(holding, Holdings)
            self.assertEqual(holding.holding_id, 1)
            self.assertEqual(holding.portfolio_id, 1)
            self.assertEqual(holding.symbol, "AMZN")
            self.assertEqual(holding.quantity, 10)
            self.assertEqual(holding.avg_buy_price, 215.00)
            
    @patch('backend.repository.Holdings_repo.Holdings_repo.add_holding')
    def test_add_holding(self, mock_add_holding):
        """Test the add holding service method."""
        mock_add_holding.return_value = 1
        result = self.holdings_service.add_holding(new_holding)
        assert isinstance(result, int)
        self.assertEqual(result, 1)

    @patch('backend.repository.Holdings_repo.Holdings_repo.update_holding')
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_holding_id')
    def test_update_holding(self, mock_get_holdings_by_holding_id, mock_update_holding):
        """Test the update holding service method."""
        existing_holding = Holdings(
            holding_id=1,
            portfolio_id=1,
            symbol="AMZN",
            quantity=5,
            avg_buy_price=200.00
        )
        
        updated_holding = Holdings(
            holding_id=1,
            portfolio_id=1,
            symbol="AMZN",
            quantity=5,
            avg_buy_price=230.00
        )
        
        mock_get_holdings_by_holding_id.return_value = existing_holding
        mock_update_holding.return_value = new_holding

        result = self.holdings_service.update_holding(updated_holding)
        assert isinstance(result, Holdings)
        self.assertEqual(result, new_holding)
        self.assertEqual(result.holding_id, 1)
        self.assertEqual(result.portfolio_id, 1)
        self.assertEqual(result.symbol, "AMZN")
        self.assertEqual(result.quantity, 10)  # Total quantity after update
        self.assertAlmostEqual(result.avg_buy_price, 215.00)  # New average buying price

    @patch('backend.repository.Holdings_repo.Holdings_repo.delete_holding')
    def test_delete_holding(self, mock_delete_holding):
        """Test the delete holding service method."""
        mock_delete_holding.return_value = 1
        result = self.holdings_service.delete_holding(1)
        assert isinstance(result, int)
        self.assertEqual(result, 1)