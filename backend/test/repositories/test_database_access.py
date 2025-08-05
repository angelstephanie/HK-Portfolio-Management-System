from backend.repository.database_access import get_database_connection

def test_get_database_connection():
    """Test the database connection function."""
    db_connection = get_database_connection()
    assert db_connection is not None, "Database connection should not be None"
    assert db_connection.is_connected(), "Database connection should be open"
    assert db_connection.database == 'hongkonghackathon', "Database name should be 'hongkonghackathon'"
    db_connection.close()

def run_tests():
    """Run all database access tests."""
    test_get_database_connection()
    print("Database access tests passed successfully!")