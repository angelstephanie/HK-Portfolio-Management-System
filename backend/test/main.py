import unittest

import backend.test.repositories.test_database_access as test_database_access

import backend.test.models.test_Transaction as test_Transaction
import backend.test.models.test_Holdings as test_Holdings
import backend.test.models.test_Asset as test_Asset
import backend.test.models.test_PortfolioSnap as test_PortfolioSnap
import backend.test.models.test_Portfolio as test_Portfolio

import backend.test.repositories.test_Asset_repo as test_Asset_repo
import backend.test.repositories.test_Holdings_repo as test_Holdings_repo
import backend.test.repositories.test_PortfolioSnap_repo as test_PortfolioSnap_repo
import backend.test.repositories.test_Portfolio_repo as test_Portfolio_repo
import backend.test.repositories.test_Transaction_repo as test_Transaction_repo

from backend.test.controllers.test_Asset_controller import TestAssetController
from backend.test.controllers.test_Holdings_controller import TestHoldingsController
from backend.test.controllers.test_Portfolio_controller import TestPortfolioController
from backend.test.controllers.test_PortfolioSnap_controller import TestPortfolioSnapController
from backend.test.controllers.test_Transaction_controller import TestTransactionController

def run_tests():
    # run database access tests
    test_database_access.run_tests()
    
    # Run models tests
    test_Asset.run_tests()
    test_Holdings.run_tests()
    test_PortfolioSnap.run_tests()
    test_Portfolio.run_tests()
    test_Transaction.run_tests()
    
    # Run repositories tests
    test_Asset_repo.run_tests()
    test_Holdings_repo.run_tests()
    test_Portfolio_repo.run_tests()
    test_PortfolioSnap_repo.run_tests()
    test_Transaction_repo.run_tests()
    
    # Run controllers tests   
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('backend/test/controllers', pattern='test_*.py')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)

if __name__ == "__main__":
    run_tests()
    # unittest.main()
    print("All tests passed successfully!")