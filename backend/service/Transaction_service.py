from repository.Transaction_repo import Transaction_repo

class TransactionService:
    def __init__(self):
        self.transaction_repo = Transaction_repo()

    def add_transaction(self, transaction):
        self.transaction_repo.add_transaction(transaction)

    def get_transactions_by_portfolio_id(self, portfolio_id: int):
        return self.transaction_repo.get_transactions_by_portfolio_id(portfolio_id)

    def delete_transaction(self, transaction_id: int):
        self.transaction_repo.delete_transaction(transaction_id)