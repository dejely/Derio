import matplotlib.pyplot as plt
from database import get_summary

def gen_output():
    summary = get_summary()
    categories = [item[0] for item in summary]
    amount = [item[1] for item in summary]

    plt.bar(categories, amount)
    plt.xlabel("Category")
    plt.ylabel("Amounts")
    plt.title("Income vs Expenses")
    plt.show()