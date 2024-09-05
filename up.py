import json
import os
from datetime import datetime
TRANS = "transactions.json"

def load_transactions():
    if os.path.exists(TRANS):
        with open(TRANS, 'r') as file:
            return json.load(file)
    return []

def save_transactions(transactions):
    with open(TRANS, 'w') as file:
        json.dump(transactions, file, indent=4)

def add_transaction(transactions, type_, category, amount):
    transaction = {
        'type': type_,
        'category': category,
        'amount': amount,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print(f"{type_.capitalize()} of {amount} added to category '{category}'.")

def calculate_budget(transactions):
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    return income, expenses, income - expenses

def expense_analysis(transactions):
    categories = {}
    for t in transactions:
        if t['type'] == 'expense':
            categories[t['category']] = categories.get(t['category'], 0) + t['amount']

    print("\nExpense Analysis:")
    for category, amount in categories.items():
        print(f"Category: {category}, Total Spent: {amount}")

def list_transactions(transactions):
    if not transactions:
        print("No transactions recorded.")
    else:
        for i, transaction in enumerate(transactions):
            print(f"{i + 1}. [{transaction['date']}] {transaction['type'].capitalize()}: {transaction['amount']} in {transaction['category']}")

def main():
    transactions = load_transactions()

    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. List Transactions")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            add_transaction(transactions, 'expense', category, amount)
        elif choice == '2':
            category = input("Enter income category: ")
            amount = float(input("Enter amount: "))
            add_transaction(transactions, 'income', category, amount)
        elif choice == '3':
            income, expenses, remaining = calculate_budget(transactions)
            print(f"Total Income: {income}, Total Expenses: {expenses}, Remaining Budget: {remaining}")
        elif choice == '4':
            expense_analysis(transactions)
        elif choice == '5':
            list_transactions(transactions)
        elif choice == '6':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
