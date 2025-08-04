from backend.models.Portfolio import Portfolio
from backend.repository.database_access import get_database_connection

class Portfolio_repo:
    def __init__(self):
        self.connection = get_database_connection()


    def add_portfolio(self, portfolio: Portfolio):
        """Add a new portfolio to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO Portfolios (name, description, created_at)
                VALUES (%s, %s, %s)
            """, (portfolio.name, portfolio.description, portfolio.created_at))
            self.connection.commit()
            portfolio.portfolio_id = cursor.lastrowid
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Portfolio added: {portfolio}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error adding portfolio: {e}")
            return None
        
        
    

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
            print(f"✅ Portfolio updated: {portfolio}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error updating portfolio: {e}")
            return None
        
        


    def delete_portfolio(self, portfolio_id: int):
        """Delete a portfolio by its ID."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Portfolios WHERE portfolio_id = %s", (portfolio_id,))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ Portfolio deleted: {portfolio_id}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error deleting portfolio: {e}")
            return None
        
        
    
 
    def get_portfolio_by_id(self, portfolio_id: int) -> Portfolio:
        """Retrieve a portfolio by its ID."""
        try:
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
            else:
                print(f"❌ No Portfolio found with ID: {portfolio_id}")
                return None
        except Exception as e:
            print(f"❌ Error retrieving Portfolio: {e}")
            return None


    def get_all_portfolios(self) -> list[Portfolio]:
        """Retrieve all portfolios from the database."""
        try:
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
            print(f"✅ Retrieved {len(portfolios)} Portfolios")
            return portfolios
        except Exception as e:
            print(f"❌ Error retrieving all portfolios: {e}")
            return []

