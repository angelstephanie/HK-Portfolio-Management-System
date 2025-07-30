from models.Portfolio import Portfolio
from repository.database_access import get_database_connection

class Portfolio_repo:
    def __init__(self):
        self.connection = get_database_connection()

    @staticmethod
    def create_portfolio_table(self):
        """Create the Portfolio table in the database if it does not exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Portfolios (
                    portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
            """)
            self.connection.commit()
            cursor.close()
            print("✅ Portfolio table created successfully.")
        except Exception as e:
            print(f"❌ Error creating Portfolio table: {e}")

    @staticmethod
    def add_portfolio(self, portfolio: Portfolio):
        """Add a new portfolio to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO Portfolios (name, description, created_at)
                VALUES (%s, %s, %s)
            """, (portfolio.name, portfolio.description, portfolio.created_at))
            self.connection.commit()
            portfolio.portfolio_id(cursor.lastrowid)
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Portfolio added: {portfolio.name}")
        except Exception as e:
            print(f"❌ Error adding portfolio: {e}")
        
        return affected_rows if affected_rows > 0 else None
    
    @staticmethod
    def update_portfolio(self, portfolio: Portfolio):
        """Update an existing portfolio in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Portfolios
                SET name = %s, description = %s, created_at = %s
                WHERE portfolio_id = %s
            """, (portfolio.name, portfolio.description, portfolio.created_at, portfolio.portfolio_id))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Portfolio updated: {portfolio.name}")
        except Exception as e:
            print(f"❌ Error updating portfolio: {e}")
        
        return affected_rows if affected_rows > 0 else None

    @staticmethod
    def delete_portfolio(self, portfolio_id: int):
        """Delete a portfolio by its ID."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Portfolios WHERE portfolio_id = %s", (portfolio_id,))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Portfolio deleted: {portfolio_id}")
        except Exception as e:
            print(f"❌ Error deleting portfolio: {e}")
        
        return affected_rows if affected_rows > 0 else None
    
    @staticmethod    
    def get_portfolio_by_id(self, portfolio_id: int) -> Portfolio:
        """Retrieve a portfolio by its ID."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Portfolios WHERE portfolio_id = %s", (portfolio_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return Portfolio(
                name=row[1],
                created_at=row[3],
                portfolio_id=row[0],
                description=row[2] if row[2] is not None else ""
            )
        return None

    @staticmethod
    def get_all_portfolios(self) -> list[Portfolio]:
        """Retrieve all portfolios from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Portfolios")
        rows = cursor.fetchall()
        cursor.close()
        
        portfolios = []
        for row in rows:
            portfolios.append(Portfolio(
                name=row[1],
                created_at=row[3],
                portfolio_id=row[0],
                description=row[2] if row[2] is not None else ""
            ))
        return portfolios

