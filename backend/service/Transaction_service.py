from backend.repository.Transaction_repo import Transaction_repo
from backend.models.Transaction import Transaction,TransactionType
from backend.repository.Holdings_repo import Holdings_repo
from backend.models.Holdings import Holdings
class TransactionService:
    def __init__(self):
        self.transaction_repo = Transaction_repo()
        self.holdings_repo = Holdings_repo()

    def add_transaction(self, transaction):
        if not transaction:
            raise ValueError("transaction cannot be empty")
        if not isinstance(transaction, Transaction):
            raise TypeError("transaction must be a object of Transaction")
        
        current_holdings = self.holdings_repo.get_holdings_by_symbol(transaction.symbol)
        if not current_holdings:
            self.holdings_repo.add_holding(Holdings(portfolio_id=transaction.portfolio_id, symbol=transaction.symbol, quantity=0, avg_buy_price=0))
            current_holdings = self.holdings_repo.get_holdings_by_symbol(transaction.symbol)
        
        current_quantity = current_holdings.quantity
        
        if transaction.type is TransactionType.BUY:
            updated_quantity = current_quantity + transaction.quantity
            updated_holding = Holdings(portfolio_id = current_holdings.portfolio_id, symbol= current_holdings.symbol, quantity=updated_quantity, avg_buy_price=transaction.price_per_unit, holding_id=current_holdings.holding_id)
            self.holdings_repo.update_holding(updated_holding)
            
        elif transaction.type is TransactionType.SELL:
            if current_quantity < transaction.quantity:
                raise ValueError("Insufficient quantity to sell")
            
            updated_quantity = current_quantity - transaction.quantity
            
            if updated_quantity == 0:
                self.holdings_repo.delete_holding(current_holdings.holding_id)
            else:
                updated_holding = Holdings(portfolio_id = current_holdings.portfolio_id, symbol= current_holdings.symbol, quantity=updated_quantity, avg_buy_price=transaction.price_per_unit, holding_id=current_holdings.holding_id)
                self.holdings_repo.update_holding(updated_holding)
            
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
    
    def update_transaction(self, transaction):
        if not transaction:
            raise ValueError("Transaction cannot be empty")
        if not isinstance(transaction, Transaction):
            raise TypeError("Transaction must be a object of Transaction")

        return self.transaction_repo.update_transaction(transaction)    