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
        """Test the get all holdings service method."""
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
            
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_all_holdings')
    def test_get_all_holdings_none(self, mock_get_all_holdings):
        """Test the get all holdings service method, when get_all_holdings repo method returns None due to exception."""
        mock_get_all_holdings.return_value = None
        result = self.holdings_service.get_all_holdings()
        self.assertEqual(result, None)
        
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_all_holdings')
    def test_get_all_holdings_empty_list(self, mock_get_all_holdings):
        """Test the get all holdings service method, when get_all_holdings repo method returns [] due to database access issue."""
        mock_get_all_holdings.return_value = []
        result = self.holdings_service.get_all_holdings()
        self.assertEqual(result, [])
            
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_id')
    def test_get_holdings_by_id(self, mock_get_holdings_by_id):
        """Test the get all holdings by portfolio ID service method, with correct behavior."""
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
            
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_id')
    def test_get_holdings_by_id_none(self, mock_get_holdings_by_id):
        """Test the get all holdings by portfolio ID service method,  when get_holdings_by_id repo method returns None due to exception."""
        mock_get_holdings_by_id.return_value = None
        result = self.holdings_service.get_holdings_by_id(1)
        self.assertEqual(result, None)
        
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_id')
    def test_get_holdings_by_id_empty_list(self, mock_get_holdings_by_id):
        """Test the get all holdings by portfolio ID service method,  when get_holdings_by_id repo method returns [] due to data access issue."""
        mock_get_holdings_by_id.return_value = []
        result = self.holdings_service.get_holdings_by_id(1)
        self.assertEqual(result, [])
        
    def test_get_holdings_by_id_empty(self):
        """Test the get all holdings by portfolio ID service method,  when holding_id is not passed."""
        with self.assertRaises(TypeError):
            self.holdings_service.get_holdings_by_id()
    
    def test_get_holdings_by_id_non_int(self):
        """Test the get all holdings by portfolio ID service method,  when holding_id is not of Int type."""
        with self.assertRaises(TypeError):
            self.holdings_service.get_holdings_by_id("3")
            
    @patch('backend.repository.Holdings_repo.Holdings_repo.add_holding')
    def test_add_holding(self, mock_add_holding):
        """Test the add holding service method, with correct behavior."""
        mock_add_holding.return_value = 1
        result = self.holdings_service.add_holding(new_holding)
        assert isinstance(result, int)
        self.assertEqual(result, 1)
    
    @patch('backend.repository.Holdings_repo.Holdings_repo.add_holding')
    def test_add_holding_none(self, mock_add_holding):
        """Test the add holding service method, when add_holding repo method returns None either due to exception or database insert issue."""
        mock_add_holding.return_value = None
        result = self.holdings_service.add_holding(new_holding)
        self.assertEqual(result, None)
        
    def test_add_holding_empty(self):
        """Test the add holding service method, when holding is not passed."""
        with self.assertRaises(TypeError):
            self.holdings_service.add_holding()
            
    def test_add_holding_non_holding(self):
        """Test the add holding service method, when holding is not of Holdings type."""
        with self.assertRaises(TypeError):
            self.holdings_service.add_holding("1")
    
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_symbol')
    def test_add_holding_existing(self, mock_get_holdings_by_symbol):
        """Test the add holding service method, when holding already exists."""
        mock_get_holdings_by_symbol.return_value = new_holding
        with self.assertRaises(ValueError):
            self.holdings_service.add_holding(new_holding)

    @patch('backend.repository.Holdings_repo.Holdings_repo.update_holding')
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_holding_id')
    def test_update_holding(self, mock_get_holdings_by_holding_id, mock_update_holding):
        """Test the update holding service method, with correct behavior."""
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
        
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_holding_id')
    def test_update_holding_non_existing(self, mock_get_holdings_by_holding_id):
        """Test the update holding service method, when holding does not exist."""
        mock_get_holdings_by_holding_id.return_value = None
        with self.assertRaises(ValueError):
            self.holdings_service.update_holding(new_holding)
            
    @patch('backend.repository.Holdings_repo.Holdings_repo.update_holding')
    @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_holding_id')
    def test_update_holding_none(self, mock_get_holdings_by_holding_id, mock_update_holding):
        """Test the update holding service method, when update_holding repo method returns None either due to exception or database update issue."""
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
        mock_update_holding.return_value = None
        result = self.holdings_service.update_holding(updated_holding)
        self.assertEqual(result, None)
        
    def test_update_holding_empty(self):
        """Test the update holding service method, when holding is not passed."""
        with self.assertRaises(TypeError):
            self.holdings_service.update_holding()
            
    def test_update_holding_non_holding(self):
        """Test the update holding service method, when holding is not of Holdings type."""
        with self.assertRaises(TypeError):
            self.holdings_service.update_holding("1")

    @patch('backend.repository.Holdings_repo.Holdings_repo.delete_holding')
    def test_delete_holding(self, mock_delete_holding):
        """Test the delete holding service method, with correct behavior."""
        mock_delete_holding.return_value = 1
        result = self.holdings_service.delete_holding(1)
        assert isinstance(result, int)
        self.assertEqual(result, 1)
        
    @patch('backend.repository.Holdings_repo.Holdings_repo.delete_holding')
    def test_delete_holding_none(self, mock_delete_holding):
        """Test the delete holding service method, when delete_holding repo method returns None either due to exception or database delete issue."""
        mock_delete_holding.return_value = None
        result = self.holdings_service.delete_holding(1)
        self.assertEqual(result, None)
        
    def test_delete_holding_empty(self):
        """Test the delete holding service method, when holding_id is not passed."""
        with self.assertRaises(TypeError):
            self.holdings_service.delete_holding()
            
    def test_delete_holding_non_int(self):
        """Test the update holding service method, when holding_id is not of Int type."""
        with self.assertRaises(TypeError):
            self.holdings_service.delete_holding("1")