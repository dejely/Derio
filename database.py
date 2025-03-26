import sqlite3

#Setup def case

def setup_db():
    connection = sqlite3.connect("finance.db")

    cur = connection.cursor()

    comm1 = """
                CREATE TABLE IF NOT EXISTS
                   transactions(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   type TEXT,
                   category TEXT,
                   amount REAL,
                   )
                   """ 
    
    cur.execute(comm1)

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

    comm1 = 'SELECT * FROM transactions'

    cur.execute(comm1)
    transactions = cur.fetchall()

    connection.close()
    return transactions

#Total Income and expenses
def get_summary():
    connection = sqlite3.connect("finance.db")

    cur = connection.cursor()
    
    comm1 = 'SELECT type, SUM(amount) FROM transactions GROUB by type'
    cur.execute(comm1)

    summary = cur.fetchall()

    connection.close()
    return summary