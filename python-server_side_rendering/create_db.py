import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create the Products table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Clear existing data to avoid duplicates when running the script multiple times
    cursor.execute('DELETE FROM Products')

    # Insert example data into the Products table
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    # Commit the changes to save them in the database file
    conn.commit()

    # Close the database connection
    conn.close()

# Run the create_database function when this script is executed directly
if __name__ == '__main__':
    create_database()

