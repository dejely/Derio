import sqlite3

#Setup def case

def setup_db():
    connection = sqlite3.connect("finance.db")

    cur = connection.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            category TEXT,
            amount REAL,
            date TEXT
        )
    ''')
    connection.commit()
    connection.close()


#Adding transactions
def add_transaction(type, category, amount, date):
    connection = sqlite3.connect("finance.db")

    cur = connection.cursor()
    
    comm1 = """
            INSERT INTO transactions(type, category, amount, date)
            VALUES(?, ?, ?, ?)
            """ 
    cur.execute(comm1, (type, category, amount, date))

    connection.commit()
    connection.close()

#Getting all transactions
def get_all_transactions():
    connection = sqlite3.connect("finance.db")
    
    cur = connection.cursor()

    cur.execute('SELECT * FROM transactions')
    transactions = cur.fetchall()

    connection.close()
    return transactions

#Total Income and expenses
def get_summary():
    connection = sqlite3.connect("finance.db")

    cur = connection.cursor()
    
    cur.execute('SELECT type, SUM(amount) FROM transactions GROUP BY type')

    summary = cur.fetchall()

    connection.close()
    return summary