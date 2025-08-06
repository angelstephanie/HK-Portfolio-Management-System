from backend.repository.Transaction_repo import Transaction_repo
from backend.models.Transaction import Transaction
class TransactionService:
    def __init__(self):
        self.transaction_repo = Transaction_repo()

    def add_transaction(self, transaction):
        if not transaction:
            raise ValueError("transaction cannot be empty")
        if not isinstance(transaction, Transaction):
            raise TypeError("transaction must be a object of Transaction")
        
        return self.transaction_repo.add_transaction(transaction)

    def get_transaction_by_id(self, transaction_id: int):
        if not transaction_id:
            raise ValueError("transaction_id cannot be empty")
        if not isinstance(transaction_id, int):
            raise TypeError("transaction_id must be an int")
        
        return self.transaction_repo.get_transaction_by_id(transaction_id)
    
    def get_all_transactions(self):
        return self.transaction_repo.get_all_transactions()

    def delete_transaction(self, transaction_id: int):
        if not transaction_id:
            raise ValueError("transaction_id cannot be empty")
        if not isinstance(transaction_id, int):
            raise TypeError("transaction_id must be an int")
        
        return self.transaction_repo.delete_transaction(transaction_id)