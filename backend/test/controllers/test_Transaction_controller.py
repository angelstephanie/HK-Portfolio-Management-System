import unittest
from flask import Flask 
from unittest.mock import patch, MagicMock
from backend.controller.Transaction_controller import transaction_controller
from backend.service.Transaction_service import TransactionService

class TestTransactionController(unittest.TestCase):
    """Test cases for the Transaction Controller."""
    
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(transaction_controller)
        self.transaction_service = TransactionService()
        
    @patch('backend.service.Transaction_service.TransactionService.get_all_transactions')
    def test_get_all_transactions(self, mock_get_all_transactions):
        """Test the get all transactions endpoint."""
        mock_get_all_transactions.return_value = [{'transaction_id': 1, 'portfolio_id': 1, 'symbol': 'AAPL', 'type': 'buy', 'quantity': 10, 'price_per_unit': 150.0, 'fee': 5.0, 'timestamp': '2023-10-01', 'notes': 'Test transaction'}]
        response = self.app.test_client().get('/transactions')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        
    @patch('backend.service.Transaction_service.TransactionService.get_transaction_by_id')
    def test_get_transaction_by_id(self, mock_get_transaction_by_id):
        """Test the get transaction by ID endpoint."""
        mock_get_transaction_by_id.return_value = MagicMock(to_dict=lambda: {'transaction_id': 1, 'portfolio_id': 1, 'symbol': 'AAPL', 'type': 'buy', 'quantity': 10, 'price_per_unit': 150.0, 'fee': 5.0, 'timestamp': '2023-10-01', 'notes': 'Test transaction'})
        response = self.app.test_client().get('/transactions/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['transaction_id'], 1)
        
    @patch('backend.service.Transaction_service.TransactionService.add_transaction')
    def test_add_transaction(self, mock_add_transaction):
        """Test the add transaction endpoint."""
        mock_add_transaction.return_value = MagicMock(to_dict=lambda: {'transaction_id': 2})
        response = self.app.test_client().post('/transactions', json={'portfolio_id': 1, 'symbol': 'AAPL', 'type': 'buy', 'quantity': 10, 'price_per_unit': 150.0, 'fee': 5.0, 'timestamp': '2023-10-01', 'notes': 'Test transaction'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Transaction added successfully')
    
    @patch('backend.service.Transaction_service.TransactionService.delete_transaction')
    def test_delete_transaction(self, mock_delete_transaction):
        """Test the delete transaction endpoint."""
        mock_delete_transaction.return_value = 1
        response = self.app.test_client().delete('/transactions/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Transaction deleted successfully')