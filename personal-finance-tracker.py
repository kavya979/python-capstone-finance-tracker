
print("Welcome to the Personal Finance Tracker!")

expenses = {}  

def add_expense():
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip().capitalize()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_str = input("Enter amount: ").strip()
        amount = float(amount_str)

        expense = (description, amount)

        if category not in expenses:
            expenses[category] = []
        expenses[category].append(expense)

        print("Expense added successfully.")

    except ValueError as ve:
        print(f" Invalid input: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def view_expenses(data):
    if not data:
        print(" No expenses recorded yet.")
        return

    for category, items in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in items:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary(data):
    if not data:
        print("No expenses recorded yet.")
        return

    print("\n Summary:")
    for category, items in data.items():
        total = sum(amount for _, amount in items)
        print(f"{category}: ${total:.2f}")

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
