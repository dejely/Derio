import argparse
from datetime import datetime
from database import setup_db, add_transaction, get_all_transactions
from output import gen_output

def main():

    setup_db()

main()