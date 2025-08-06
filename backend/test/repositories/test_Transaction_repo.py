from backend.repository.Transaction_repo import Transaction_repo
from backend.models.Transaction import Transaction,TransactionType
from datetime import datetime

def setup():
    global transaction_repo
    transaction_repo = Transaction_repo()
    global transaction_date
    transaction_date = datetime.strptime("2023-12-02 12:00:00", "%Y-%m-%d %H:%M:%S")
    global new_transaction
    new_transaction = Transaction(
        portfolio_id=1,
        symbol="AAPL",
        quantity=10,
        price_per_unit=100.00,
        type=TransactionType.BUY,
        fee=5.00    
        )
    
def test_add_transaction():
    transaction_add = transaction_repo.add_transaction(new_transaction)
    
    assert transaction_add is not None
    assert isinstance(transaction_add, int)    
    assert transaction_add == 1

def test_get_transaction_by_id():
    transaction_id = 2
    transaction = transaction_repo.get_transaction_by_id(transaction_id)
    
    assert transaction is not None
    assert isinstance(transaction, Transaction)
    assert transaction.portfolio_id == new_transaction.portfolio_id
    assert transaction.symbol == new_transaction.symbol
    assert transaction.quantity == new_transaction.quantity
    assert transaction.price_per_unit == new_transaction.price_per_unit
    assert transaction.type == new_transaction.type

def test_get_all_transactions():
    transactions = transaction_repo.get_all_transactions()
    
    assert isinstance(transactions, list)
    assert len(transactions) > 0
    
        
    
def test_update_transaction():
    # Update the transaction's quantity
    new_transaction.quantity += 5
    updated_count = transaction_repo.update_transaction(new_transaction)
    
    assert updated_count is not None
    assert isinstance(updated_count, int)
    assert updated_count == 1
    
    # Verify the update
    transaction = transaction_repo.get_transaction_by_id(new_transaction.transaction_id)
    assert transaction.quantity == new_transaction.quantity

def test_delete_transaction():
    transaction_id = new_transaction.transaction_id
    deleted_count = transaction_repo.delete_transaction(transaction_id)
    
    assert deleted_count is not None
    assert isinstance(deleted_count, int)
    assert deleted_count == 1
    
    # Verify the deletion
    transaction = transaction_repo.get_transaction_by_id(transaction_id)
    assert transaction is None

def run_tests():
    setup()
    test_add_transaction()
    test_get_transaction_by_id()
    test_get_all_transactions()
    test_update_transaction()
    test_delete_transaction()
    print("All Transaction Repository tests passed!")