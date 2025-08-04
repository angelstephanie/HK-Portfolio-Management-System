import backend.test.models.test_Transaction
import backend.test.models.test_Holdings
import backend.test.models.test_Asset
import backend.test.models.test_PortfolioSnap
import backend.test.models.test_Portfolio

import backend.test.repositories.test_Asset_repo
import backend.test.repositories.test_Holdings_repo
import backend.test.repositories.test_PortfolioSnap_repo
import backend.test.repositories.test_Portfolio_repo
import backend.test.repositories.test_Transaction_repo

def run_tests():
    
    # Run models tests
    backend.test.model.test_Asset.run_tests()
    backend.test.model.test_Holdings.run_tests()
    backend.test.model.test_PortfolioSnap.run_tests()
    backend.test.model.test_Portfolio.run_tests()
    backend.test.model.test_Transaction.run_tests()

if __name__ == "__main__":
    run_tests()
    print("All tests passed successfully!")