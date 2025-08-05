import mysql.connector

def get_database_connection(host='localhost', user='root', password='n3u3da!', database='hongkonghackathon'):
    """Establish a connection to the MySQL database."""
    try:
        mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
if __name__ == "__main__":
    db_connection = get_database_connection()
    if db_connection:
        print("Database connection established successfully.")
        print(db_connection.database)
        db_connection.close()
    else:
        print("Failed to connect to the database.")