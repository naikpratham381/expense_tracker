expenses = []

def add_expense():
    amount = float(input("Enter amount spent: "))
    category = input("Enter category (e.g. Food, Travel): ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully! ✅")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\n----- All Expenses -----")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. ₹{expense['amount']} | {expense['category']} | {expense['description']}")

while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Total spending feature coming soon!")
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")