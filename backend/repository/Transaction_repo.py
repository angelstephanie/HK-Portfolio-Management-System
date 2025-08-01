from backend.models.Transaction import Transaction, TransactionType
from backend.repository.database_access import get_database_connection
class Transaction_repo:
    def __init__(self):
        self.connection = get_database_connection()

    

    def add_transaction(self, transaction: Transaction):
        """Add a new transaction to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO Transactions (portfolio_id, symbol, type, quantity, price_per_unit, fee, timestamp, notes)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (transaction.portfolio_id, transaction.symbol, transaction.type.value, transaction.quantity, transaction.price_per_unit, transaction.fee, transaction.timestamp, transaction.notes))
            self.connection.commit()
            transaction.transaction_id(cursor.lastrowid)
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Transaction added: {transaction.transaction_id}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error adding transaction: {e}")
        
        
    

    def update_transaction(self, transaction: Transaction):
        """Update an existing transaction in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Transactions
                SET portfolio_id = %s, symbol = %s, type = %s, quantity = %s, price_per_unit = %s, fee = %s, timestamp = %s, notes = %s
                WHERE transaction_id = %s
            """, (transaction.portfolio_id, transaction.symbol, transaction.type.value, transaction.quantity,
                  transaction.price_per_unit, transaction.fee, transaction.timestamp, transaction.notes, transaction.transaction_id))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Transaction updated: {transaction.transaction_id}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error updating transaction: {e}")
        
        
    
     
    def delete_transaction(self, transaction_id: int):
        """Delete a transaction by its ID."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Transactions WHERE transaction_id = %s", (transaction_id,))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Transaction deleted: {transaction_id}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error deleting transaction: {e}")
        
        
    
  
    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        """Retrieve a transaction by its ID."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Transactions WHERE transaction_id = %s", (transaction_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return Transaction(
                transaction_id=row[0],
                portfolio_id=row[1],
                symbol=row[2],
                type=TransactionType(row[3]),
                quantity=row[4],
                price_per_unit=row[5],
                fee=row[6],
                timestamp=row[7],
                notes=row[8]
            )

        return None
    

    def get_all_transactions(self) -> list[Transaction]:
        """Retrieve all transactions from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Transactions")
        rows = cursor.fetchall()
        cursor.close()
        
        transactions = []
        for row in rows:
            transactions.append(Transaction(
                transaction_id=row[0],
                portfolio_id=row[1],
                symbol=row[2],
                type=TransactionType(row[3]),
                quantity=row[4],
                price_per_unit=row[5],
                fee=row[6] if row[6] is not None else 0.0,
                timestamp=row[7],
                notes=row[8] if row[8] is not None else ""
            ))
        return transactions
    