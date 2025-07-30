from backend.repository.Transaction_repo import Transaction_repo

class TransactionService:
    def __init__(self):
        self.transaction_repo = Transaction_repo()

    def add_transaction(self, transaction):
        self.transaction_repo.add_transaction(transaction)

    def get_transaction_by_id(self, transaction_id: int):
        return self.transaction_repo.get_transaction_by_id(transaction_id)
    
    def get_all_transactions(self):
        return self.transaction_repo.get_all_transactions()

    def delete_transaction(self, transaction_id: int):
        self.transaction_repo.delete_transaction(transaction_id)