class FinanceTracker:
    def __init__(self):
        self.transactions = []  # Bu satır transactions listesini başlatır

    def add_transaction(self, description, amount, category):
        transaction = {'description': description, 'amount': amount, 'category': category}
        self.transactions.append(transaction)
        print(f"Transaction added: {description}, Amount: {amount}, Category: {category}")

    def get_balance(self):
        balance = sum(transaction['amount'] for transaction in self.transactions)
        return balance

    def show_transactions(self):
        for transaction in self.transactions:
            print(
                f"{transaction['description']} | Amount: {transaction['amount']} | Category: {transaction['category']}")

    def get_transactions_by_category(self, category):
        transactions = [transaction for transaction in self.transactions if
                        transaction['category'].lower() == category.lower()]
        for transaction in transactions:
            print(
                f"{transaction['description']} | Amount: {transaction['amount']} | Category: {transaction['category']}")


def main():
    tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income/Expense")
        print("2. Show All Transactions")
        print("3. Show Balance")
        print("4. Show Transactions by Category")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Description: ")
            amount = float(input("Amount (use '-' for expenses): "))
            category = input("Category: ")
            tracker.add_transaction(description, amount, category)
        elif choice == '2':
            tracker.show_transactions()
        elif choice == '3':
            print(f"Current Balance: {tracker.get_balance()}")
        elif choice == '4':
            category = input("Enter category: ")
            tracker.get_transactions_by_category(category)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
