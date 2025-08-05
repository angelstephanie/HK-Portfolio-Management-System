from backend.models.PortfolioSnap import PortfolioSnap
from backend.repository.database_access import get_database_connection
from datetime import datetime

class PortfolioSnap_repo:
    def __init__(self):
        self.connection = get_database_connection()

    
    def add_portfolio_snap(self, portfolio_snap: PortfolioSnap):
        """Add a new portfolio snapshot to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO PortfolioSnaps (portfolio_id, snapshot_date, cash_value, invested_value)
                VALUES (%s, %s, %s, %s)
            """, (portfolio_snap.portfolio_id, portfolio_snap.snapshot_date, portfolio_snap.cash_value, portfolio_snap.invested_value))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ PortfolioSnap added: {portfolio_snap}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error adding PortfolioSnap: {e}")
            return None
        
        
    
    def update_portfolio_snap(self, portfolio_snap: PortfolioSnap):
        """Update an existing portfolio snapshot in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE PortfolioSnaps
                SET cash_value = %s, invested_value = %s
                WHERE portfolio_id = %s AND snapshot_date = %s
            """, (portfolio_snap.cash_value, portfolio_snap.invested_value, portfolio_snap.portfolio_id, portfolio_snap.snapshot_date))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ PortfolioSnap updated: {portfolio_snap}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error updating PortfolioSnap: {e}")
            return None
        
       
    
    def get_portfolio_snap_by_id(self, portfolio_id: int, snapshot_date: datetime):
        """Retrieve a portfolio snapshot by portfolio ID and snapshot date."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM PortfolioSnaps
                WHERE portfolio_id = %s AND snapshot_date = %s
            """, (portfolio_id, snapshot_date))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return PortfolioSnap(
                    portfolio_id=result[0],
                    snapshot_date=result[1],
                    cash_value=result[2],
                    invested_value=result[3]
                )
            else:
                print(f"❌ No PortfolioSnap found for portfolio_id: {portfolio_id} on {snapshot_date}")
                return None
        except Exception as e:
            print(f"❌ Error retrieving PortfolioSnap: {e}")
            return None
    
    def get_all_portfolio_snaps(self):
        """Retrieve all portfolio snapshots."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM PortfolioSnaps")
            results = cursor.fetchall()
            cursor.close()
            portfolio_snaps = []
            for row in results:
                portfolio_snaps.append(PortfolioSnap(
                    portfolio_id=row[0],
                    snapshot_date=row[1],
                    cash_value=row[2],
                    invested_value=row[3]
                ))
            print(f"✅ Retrieved {len(portfolio_snaps)} PortfolioSnaps")
            return portfolio_snaps
        except Exception as e:
            print(f"❌ Error retrieving all PortfolioSnaps: {e}")
            return []
    
    def delete_portfolio_snap(self, portfolio_id: int, snapshot_date: datetime):
        """Delete a portfolio snapshot by portfolio ID and snapshot date."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                DELETE FROM PortfolioSnaps
                WHERE portfolio_id = %s AND snapshot_date = %s
            """, (portfolio_id, snapshot_date))
            self.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            print(f"✅ PortfolioSnap deleted: {portfolio_id} on {snapshot_date}")
            
            return affected_rows if affected_rows > 0 else None
        except Exception as e:
            print(f"❌ Error deleting PortfolioSnap: {e}")
            return None