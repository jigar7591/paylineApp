# database_setup.py
import sqlite3

def setup_database():
    conn = sqlite3.connect('customer_service.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE customers
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  card_number TEXT,
                  membership_no TEXT,
                  address TEXT,
                  dob TEXT,
                  outstanding REAL)''')

    # Insert sample data
    customers = [
        ('John Doe', '1234-5678-9123-4567', 'M12345', '123 Elm St', '1985-10-10', 100.0),
        ('Jane Smith', '9876-5432-1987-6543', 'M54321', '456 Oak St', '1990-05-05', 250.0),
         ('Sagar Patel', '9876-5432-1987-6543', 'M54321', '456 Oak St', '1990-05-05', 250.0),
    ]

    c.executemany('INSERT INTO customers (name, card_number, membership_no, address, dob, outstanding) VALUES (?,?,?,?,?,?)', customers)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()

