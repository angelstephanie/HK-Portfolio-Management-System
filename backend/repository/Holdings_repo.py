from models.Holdings import Holdings
from repository.database_access import get_database_connection

class Holdings_repo:
    def __init__(self):
        self.connection = get_database_connection()

    @staticmethod
    def create_holdings_table(self):
        """Create the Holdings table in the database if it does not exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Holdings (
                    holding_id INT AUTO_INCREMENT PRIMARY KEY,
                    portfolio_id INT NOT NULL,
                    symbol VARCHAR(20) NOT NULL,
                    quantity DECIMAL(15, 6) NOT NULL, 
                    avg_buy_price DECIMAL(15, 2) NOT NULL,
                    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id),
                    FOREIGN KEY (symbol) REFERENCES Assets(symbol)
                );
            """)
            self.connection.commit()
            cursor.close()
            print("✅ Holdings table created successfully.")
        except Exception as e:
            print(f"❌ Error creating Holdings table: {e}")

    @staticmethod
    def add_holding(self, holding: Holdings):
        """Add a new holding to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO Holdings (portfolio_id, symbol, quantity, avg_buy_price)
                VALUES (%s, %s, %s, %s)
            """, (holding.portfolio_id, holding.symbol, holding.quantity, holding.avg_buy_price))
            self.connection.commit()
            holding.holding_id(cursor.lastrowid)
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Holding added: {holding}")
        except Exception as e:
            print(f"❌ Error adding holding: {e}")
        
        return affected_rows if affected_rows > 0 else None
    
    @staticmethod        
    def update_holding(self, holding: Holdings):
        """Update an existing holding in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Holdings
                SET portfolio_id = %s, symbol = %s, quantity = %s, avg_buy_price = %s
                WHERE holding_id = %s
            """, (holding.portfolio_id, holding.symbol, holding.quantity, holding.avg_buy_price, holding.holding_id))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Holding updated: {holding}")
        except Exception as e:
            print(f"❌ Error updating holding: {e}")
        
        return affected_rows if affected_rows > 0 else None
    
    @staticmethod
    def delete_holding(self, holding_id: int):
        """Delete a holding by its ID."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Holdings WHERE holding_id = %s", (holding_id,))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Holding deleted: {holding_id}")
        except Exception as e:
            print(f"❌ Error deleting holding: {e}")
        
        return affected_rows if affected_rows > 0 else None
            
    def get_holdings_by_id(self, holding_id: int) -> Holdings:
        """Retrieve holdings by portfolio ID."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Holdings WHERE holding_id = %s", (holding_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return Holdings(
                holding_id=row[0],
                portfolio_id=row[1],
                symbol=row[2],
                quantity=row[3],
                avg_buy_price=row[4]
            )
        return None
    
    @staticmethod
    def get_all_holdings(self) -> list[Holdings]:
        """Retrieve all holdings from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Holdings")
        rows = cursor.fetchall()
        cursor.close()
        
        holdings_list = []
        for row in rows:
            holdings_list.append(Holdings(
                holding_id=row[0],
                portfolio_id=row[1],
                symbol=row[2],
                quantity=row[3],
                avg_buy_price=row[4]
            ))
        return holdings_list