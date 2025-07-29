from models.Transaction import Transaction
from repository.database_access import get_database_connection
class Transaction_repo:
    def __init__(self):
        self.connection = get_database_connection()
    def create_transaction_table(self):
        pass
    
    def add_transaction(self, transaction: Transaction):
        pass
    
    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        pass
    
    def get_all_transactions(self) -> list[Transaction]:
        pass
    
    def delete_transaction(self, transaction_id: int):
        pass