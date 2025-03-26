import argparse
from datetime import datetime
from database import setup_db, add_transaction, get_all_transactions
from output import gen_output

def main():

    setup_db()

    parser = argparse.ArgumentParser(description="Personal Finance Manager")
    
    # Commands
    parser.add_argument('--add', help="Add a new transaction", action="store_true")
    parser.add_argument('--report', help="Generate a report", action="store_true")
    parser.add_argument('--list', help="List all transactions", action="store_true")
    
    # Arguments for adding transactions
    parser.add_argument('--type', help="Type of transaction: income/expense", choices=['income', 'expense'])
    parser.add_argument('--category', help="Category of the transaction (e.g., 'Groceries', 'Salary')")
    parser.add_argument('--amount', help="Amount of the transaction", type=float)
    parser.add_argument('--date', help="Date of the transaction (default: today)", default=datetime.now().strftime('%Y-%m-%d'))

    args = parser.parse_args()

    # Adding a transaction
    if args.add:
        if not (args.type and args.category and args.amount):
            print("Error: Please provide the transaction type, category, and amount.")
            return
        
        add_transaction(args.type, args.category, args.amount, args.date)
        print(f"{args.type.capitalize()} of ${args.amount} added under category '{args.category}' on {args.date}.")
    
    # Generating a report
    elif args.report:
        print("Generating financial report...")
        gen_output()
    
    # Listing all transactions
    elif args.list:
        transactions = get_all_transactions()
        if not transactions:
            print("No transactions found.")
        else:
            for transaction in transactions:
                print(f"{transaction[1].capitalize()} - {transaction[2]}: ${transaction[3]} on {transaction[4]}")
    
    else:
        print("Please specify a command. Use --help for available options.")


main()