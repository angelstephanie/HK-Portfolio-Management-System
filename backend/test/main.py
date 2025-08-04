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

def run_tests():
    
    # Run models tests
    test_Asset.run_tests()
    test_Holdings.run_tests()
    test_PortfolioSnap.run_tests()
    test_Portfolio.run_tests()
    test_Transaction.run_tests()
    
    # Run repositories tests
    test_Asset_repo.run_tests()
    test_Holdings_repo.run_tests()

if __name__ == "__main__":
    run_tests()
    print("All tests passed successfully!")