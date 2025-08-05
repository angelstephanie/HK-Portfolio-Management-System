import unittest
from flask import Flask
from unittest.mock import patch, MagicMock
from backend.controller.PortfolioSnap_controller import portfolio_snap_controller
from backend.service.PortfolioSnap_service import PortfolioSnapService

class TestPortfolioSnapController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(portfolio_snap_controller)
        self.client = self.app.test_client()

    @patch.object(PortfolioSnapService, 'get_all_portfolio_snaps')
    def test_get_all_portfolio_snaps(self, mock_get_all_portfolio_snaps):
        mock_get_all_portfolio_snaps.return_value = [
            MagicMock(to_dict=lambda: {'portfolio_id': 1, 'snapshot_date': '2023-01-01', 'cash_value': 150000.0, 'invested_value': 200000.0}),
            MagicMock(to_dict=lambda: {'portfolio_id': 1, 'snapshot_date': '2023-01-02', 'cash_value': 155000.0, 'invested_value': 250000.0})
        ]
        response = self.client.get('/portfolio_snaps')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [
            {'portfolio_id': 1, 'snapshot_date': '2023-01-01', 'cash_value': 150000.0, 'invested_value': 200000.0},
            {'portfolio_id': 1, 'snapshot_date': '2023-01-02', 'cash_value': 155000.0, 'invested_value': 250000.0}
            ])

    @patch.object(PortfolioSnapService, 'get_portfolio_snap_by_id')
    def test_get_portfolio_snap_by_id_found(self, mock_get_portfolio_snap_by_id):
        mock_get_portfolio_snap_by_id.return_value = MagicMock(to_dict=lambda: {'portfolio_id': 1, 'snapshot_date': '2023-01-01', 'cash_value': 150000.0, 'invested_value': 200000.0})
        response = self.client.get('/portfolio_snaps/1/2023-01-01')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'portfolio_id': 1, 'snapshot_date': '2023-01-01', 'cash_value': 150000.0, 'invested_value': 200000.0})

    @patch.object(PortfolioSnapService, 'get_portfolio_snap_by_id')
    def test_get_portfolio_snap_by_id_not_found(self, mock_get_portfolio_snap_by_id):
        mock_get_portfolio_snap_by_id.return_value = None
        response = self.client.get('/portfolio_snaps/1/2023-01-01')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': 'Portfolio Snap not found'})

    @patch.object(PortfolioSnapService, 'add_portfolio_snap')
    def test_add_portfolio_snap_success(self, mock_add_portfolio_snap):
        mock_add_portfolio_snap.return_value = True
        response = self.client.post('/portfolio_snaps', json={'portfolio_id': 1, 'snapshot_date': '2023-01-01', 'cash_value': 150000.0, 'invested_value': 200000.0})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'Portfolio Snap added successfully'})

    @patch.object(PortfolioSnapService, 'add_portfolio_snap')
    def test_add_portfolio_snap_failure(self, mock_add_portfolio_snap):
        mock_add_portfolio_snap.return_value = False
        response = self.client.post('/portfolio_snaps', json={'portfolio_id': 1, 'snapshot_date': '2023-01-01', 'cash_value': 150000.0, 'invested_value': 200000.0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Failed to add Portfolio Snap'})

    @patch.object(PortfolioSnapService, 'update_portfolio_snap')
    def test_update_portfolio_snap_success(self, mock_update_portfolio_snap):
        mock_update_portfolio_snap.return_value = True
        response = self.client.put('/portfolio_snaps', json={'portfolio_id': 1, 'snapshot_date': '2023-01-01', 'cash_value': 150000.0, 'invested_value': 200000.0})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Portfolio Snap updated successfully'})

    @patch.object(PortfolioSnapService, 'update_portfolio_snap')
    def test_update_portfolio_snap_not_found(self, mock_update_portfolio_snap):
        mock_update_portfolio_snap.return_value = False
        response = self.client.put('/portfolio_snaps', json={'portfolio_id': 1, 'snapshot_date': '2023-01-01', 'cash_value': 150000.0, 'invested_value': 200000.0})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': 'Portfolio Snap not found'})
