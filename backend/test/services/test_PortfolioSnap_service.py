import unittest
from flask import Flask
from unittest.mock import patch
from backend.service.PortfolioSnap_service import PortfolioSnapService
from backend.repository.PortfolioSnap_repo import PortfolioSnap_repo
from backend.models.PortfolioSnap import PortfolioSnap
from datetime import datetime

class TestPortfolioSnapService(unittest.TestCase):
    """Test cases for the PortfolioSnap Service."""
    
    def setUp(self):
        self.app = Flask(__name__)
        self.portfolio_snap_service = PortfolioSnapService()
        self.portfolio_snap_repo = PortfolioSnap_repo()
        global new_portfolio_snap
        global date
        date = datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
        new_portfolio_snap = PortfolioSnap(
            portfolio_id=1,
            snapshot_date=date,
            cash_value=10000.00,
            invested_value=1500.00
        )
        
    @patch('backend.repository.PortfolioSnap_repo.PortfolioSnap_repo.get_all_portfolio_snaps')
    def test_get_all_portfolio_snaps(self, mock_get_all_portfolio_snaps):
        """Test the get all portfolio snaps service method, with correct behavior."""
        mock_get_all_portfolio_snaps.return_value = [new_portfolio_snap]
        result = self.portfolio_snap_service.get_all_portfolio_snaps()
        assert isinstance(result, list)
        self.assertEqual(result, [new_portfolio_snap])
        assert len(result) > 0
    
        for snap in result:
            assert isinstance(snap, PortfolioSnap)
            self.assertEqual(snap.portfolio_id, 1)
            self.assertEqual(snap.cash_value, 10000.0)
            self.assertEqual(snap.invested_value, 1500.0)
            
    @patch('backend.repository.PortfolioSnap_repo.PortfolioSnap_repo.get_all_portfolio_snaps')
    def test_get_all_portfolio_snaps_none(self, mock_get_all_portfolio_snaps):
        """Test the get all portfolio snaps service method, when get_all_portfolio_snaps repo method returns None due to exception."""
        mock_get_all_portfolio_snaps.return_value = None
        result = self.portfolio_snap_service.get_all_portfolio_snaps()
        self.assertEqual(result, None)
        
    @patch('backend.repository.PortfolioSnap_repo.PortfolioSnap_repo.get_all_portfolio_snaps')
    def test_get_all_portfolio_snaps_empty_list(self, mock_get_all_portfolio_snaps):
        """Test the get all portfolio snaps service method, when get_all_portfolio_snaps repo method returns [] due to database select issue."""
        mock_get_all_portfolio_snaps.return_value = []
        result = self.portfolio_snap_service.get_all_portfolio_snaps()
        self.assertEqual(result, [])
            
    @patch('backend.repository.PortfolioSnap_repo.PortfolioSnap_repo.get_portfolio_snap_by_id')
    def test_get_portfolio_snap_by_id(self, mock_get_portfolio_snap_by_id):
        """Test the get portfolio snap by ID service method, with correct behavior."""
        mock_get_portfolio_snap_by_id.return_value = new_portfolio_snap
        result = self.portfolio_snap_service.get_portfolio_snap_by_id(1, date)
        self.assertEqual(result, new_portfolio_snap)
        assert isinstance(result, PortfolioSnap)
        self.assertEqual(result.portfolio_id, 1)
        self.assertEqual(result.cash_value, 10000.0)
        self.assertEqual(result.invested_value, 1500.0)
        
    @patch('backend.repository.PortfolioSnap_repo.PortfolioSnap_repo.get_portfolio_snap_by_id')
    def test_get_portfolio_snap_by_id_none(self, mock_get_portfolio_snap_by_id):
        """Test the get portfolio snap by ID service method, when get_portfolio_by_snap_id returns None either due to exception or database select issue."""
        mock_get_portfolio_snap_by_id.return_value = None
        result = self.portfolio_snap_service.get_portfolio_snap_by_id(1, date)
        self.assertEqual(result, None)
        
    def test_get_portfolio_snap_by_id_empty_id(self):
        """Test the update portfolio service method, when snap_id is not passed."""
        with self.assertRaises(TypeError):
            self.portfolio_snap_service.get_portfolio_snap_by_id(snap_date=date)
            
    def test_get_portfolio_snap_by_id_empty_date(self):
        """Test the update portfolio service method, when snap_date is not passed."""
        with self.assertRaises(TypeError):
            self.portfolio_snap_service.get_portfolio_snap_by_id(snap_id=1)
            
    def test_get_portfolio_snap_by_id_none_id(self):
        """Test the update portfolio service method, when snap_id is None."""
        with self.assertRaises(ValueError):
            self.portfolio_snap_service.get_portfolio_snap_by_id(None, date)
            
    def test_get_portfolio_snap_by_id_none_date(self):
        """Test the update portfolio service method, when snap_date is None."""
        with self.assertRaises(ValueError):
            self.portfolio_snap_service.get_portfolio_snap_by_id(1, None)
            
    def test_get_portfolio_snap_by_id_non_int(self):
        """Test the update portfolio service method, when snap_id is not of Int type."""
        with self.assertRaises(TypeError):
            self.portfolio_snap_service.get_portfolio_snap_by_id("1", date)
            
    def test_get_portfolio_snap_by_id_non_datetime(self):
        """Test the update portfolio service method, when snap_id is not of Datetime type."""
        with self.assertRaises(TypeError):
            self.portfolio_snap_service.get_portfolio_snap_by_id(1, 2025)

    @patch('backend.repository.PortfolioSnap_repo.PortfolioSnap_repo.update_portfolio_snap')
    def test_update_portfolio_snap(self, mock_update_portfolio_snap):
        """Test the update portfolio snap service method, with correct behavior."""
        mock_update_portfolio_snap.return_value = 1
        result = self.portfolio_snap_service.update_portfolio_snap(new_portfolio_snap)
        assert isinstance(result, int)
        self.assertEqual(result, 1)
        
    @patch('backend.repository.PortfolioSnap_repo.PortfolioSnap_repo.update_portfolio_snap')
    def test_update_portfolio_snap_none(self, mock_update_portfolio_snap):
        """Test the update portfolio snap service method, when update_portfolio repo method returns None either due to exception or database update issue."""
        mock_update_portfolio_snap.return_value = None
        result = self.portfolio_snap_service.update_portfolio_snap(new_portfolio_snap)
        self.assertEqual(result, None)
        
    def test_update_portfolio_snap_empty(self):
        """Test the update portfolio snap service method, when portfolio_snap is not passed."""
        with self.assertRaises(TypeError):
            self.portfolio_snap_service.update_portfolio_snap()
            
    def test_update_portfolio_none_parameter(self):
        """Test the update portfolio snap service method, when portfolio_snap None."""
        with self.assertRaises(ValueError):
            self.portfolio_snap_service.update_portfolio_snap(None)
            
    def test_update_portfolio_snap_non_portfolio_snap(self):
        """Test the update portfolio snap service method, when portfolio_snap is not of PorfolioSnap type."""
        with self.assertRaises(TypeError):
            self.portfolio_snap_service.update_portfolio_snap("1")
        
    @patch('backend.repository.PortfolioSnap_repo.PortfolioSnap_repo.add_portfolio_snap')
    def test_add_portfolio_snap(self, mock_add_portfolio_snap):
        """Test the add portfolio snap service method."""
        mock_add_portfolio_snap.return_value = 1
        result = self.portfolio_snap_service.add_portfolio_snap(new_portfolio_snap)
        assert isinstance(result, int)
        self.assertEqual(result, 1)

    def test_add_portfolio_snap_empty(self):
        """Test the add portfolio snap service method, when portfolio_snap is not passed."""
        with self.assertRaises(TypeError):
            self.portfolio_snap_service.add_portfolio_snap()
            
    def test_add_portfolio_snap_none(self):
        """Test the add portfolio snap service method, when portfolio_snap is None."""
        with self.assertRaises(ValueError):
            self.portfolio_snap_service.add_portfolio_snap(None)
            
    def test_add_portfolio_snap_non_portfolio_snap(self):
        """Test the add portfolio snap service method, when portfolio_snap is not of PortfolioSnap type.""" 
        with self.assertRaises(TypeError):
            self.portfolio_snap_service.add_portfolio_snap("invalid_object")