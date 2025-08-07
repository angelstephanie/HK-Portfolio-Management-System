import unittest
from unittest.mock import patch
from backend.service.Transaction_service import TransactionService
from backend.repository.Transaction_repo import Transaction_repo
from backend.models.Transaction import Transaction, TransactionType
from backend.models.Holdings import Holdings

class TestTransactionService(unittest.TestCase):
    """Test cases for the Transaction Service."""
    
    def setUp(self):
        self.transaction_service = TransactionService()
        self.transaction_repo = Transaction_repo()
        global new_transaction
        new_transaction = Transaction(
            transaction_id=1,
            portfolio_id=1,
            symbol="AAPL",
            type=TransactionType.BUY,
            quantity=10,
            price_per_unit=100.00,
        )
        
    @patch('backend.repository.Transaction_repo.Transaction_repo.get_all_transactions')
    def test_get_all_transactions(self, mock_get_all_transactions):
        """Test the get all transactions service method, with correct behavior."""
        mock_get_all_transactions.return_value = [new_transaction]
        result = self.transaction_service.get_all_transactions()
        assert isinstance(result, list)
        self.assertEqual(result, [new_transaction])
        assert len(result) > 0
    
        for transaction in result:
            assert isinstance(transaction, Transaction)
            self.assertEqual(transaction.transaction_id, 1)
            self.assertEqual(transaction.portfolio_id, 1)
            self.assertEqual(transaction.symbol, "AAPL")
            self.assertEqual(transaction.type, TransactionType.BUY)
            self.assertEqual(transaction.quantity, 10)
            self.assertEqual(transaction.price_per_unit, 100.0)
            
    @patch('backend.repository.Transaction_repo.Transaction_repo.get_all_transactions')
    def test_get_all_transactions_none(self, mock_get_all_transactions):
        """Test the get all transactions service method, when get_all_transactions repo method returns None due to exception."""
        mock_get_all_transactions.return_value = None
        result = self.transaction_service.get_all_transactions()
        self.assertEqual(result, None)
        
    @patch('backend.repository.Transaction_repo.Transaction_repo.get_all_transactions')
    def test_get_all_transactions_empty_list(self, mock_get_all_transactions):
        """Test the get all transactions service method, when get_all_transactions repo method returns [] due to database select issue."""
        mock_get_all_transactions.return_value = []
        result = self.transaction_service.get_all_transactions()
        self.assertEqual(result, [])
            
    @patch('backend.repository.Transaction_repo.Transaction_repo.get_transaction_by_id')
    def test_get_transaction_by_id(self, mock_get_transaction_by_id):
        """Test the get transaction by ID service method, with correct behavior."""
        mock_get_transaction_by_id.return_value = new_transaction
        result = self.transaction_service.get_transaction_by_id(1)
        self.assertEqual(result, new_transaction)
        assert isinstance(result, Transaction)
        self.assertEqual(result.transaction_id, 1)
        self.assertEqual(result.portfolio_id, 1)
        self.assertEqual(result.symbol, "AAPL")
        self.assertEqual(result.type, TransactionType.BUY)
        self.assertEqual(result.quantity, 10)
        self.assertEqual(result.price_per_unit, 100.0)
        
    @patch('backend.repository.Transaction_repo.Transaction_repo.get_transaction_by_id')
    def test_get_transaction_by_id_none(self, mock_get_transaction_by_id):
        """Test the get transaction by ID service method, when get_transaction_by_id returns None either due to exception or database select issue."""
        mock_get_transaction_by_id.return_value = None
        result = self.transaction_service.get_transaction_by_id(1)
        self.assertEqual(result, None)
        
    def test_get_transaction_by_id_empty(self):
        """Test the get transaction by id service method, when transaction_id is not passed."""
        with self.assertRaises(TypeError):
            self.transaction_service.get_transaction_by_id()
            
    def test_get_transaction_by_id_none_parameter(self):
        """Test the get transaction by id service method, when transaction_id is None."""
        with self.assertRaises(ValueError):
            self.transaction_service.get_transaction_by_id(None)
            
    def test_get_transaction_by_id_non_int(self):
        """Test the get transaction by id service method, when transaction_id is not of Int type."""
        with self.assertRaises(TypeError):
            self.transaction_service.get_transaction_by_id("1")

    # @patch('backend.repository.Holdings_repo.Holdings_repo.get_holdings_by_symbol')
    # @patch('backend.repository.Transaction_repo.Transaction_repo.add_transaction')
    # def test_add_transaction(self, mock_add_transaction, mock_get_holdings_by_symbol):
    #     """Test the add transaction service method, with correct behavior."""
    #     current_holding = Holdings(
    #         holding_id=1,
    #         portfolio_id=1,
    #         symbol="AMZN",
    #         quantity=10,
    #         avg_buy_price=215.00
    #     )
    #     mock_get_holdings_by_symbol.return_value = current_holding
    #     mock_add_transaction.return_value = 1
    #     result = self.transaction_service.add_transaction(new_transaction)
    #     assert isinstance(result, int)
    #     self.assertEqual(result, 1)

    @patch('backend.repository.Transaction_repo.Transaction_repo.delete_transaction')
    def test_delete_transaction(self, mock_delete_transaction):
        """Test the delete transaction service method."""
        mock_delete_transaction.return_value = 1
        result = self.transaction_service.delete_transaction(1)
        assert isinstance(result, int)
        self.assertEqual(result, 1)
