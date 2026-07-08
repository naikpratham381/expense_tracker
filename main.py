import csv
import os

expenses = []
FILE_PATH = "data/expenses.csv"


def save_expenses():
    os.makedirs("data", exist_ok=True)

    with open(FILE_PATH, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "description"])
        writer.writeheader()
        writer.writerows(expenses)


def load_expenses():
    if not os.path.exists(FILE_PATH):
        return

    with open(FILE_PATH, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)


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
    save_expenses()
    print("Expense added successfully! ✅")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\n----- All Expenses -----")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. ₹{expense['amount']} | {expense['category']} | {expense['description']}")


def total_spending():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    total = 0
    for expense in expenses:
        total = total + expense['amount']

    print(f"\n💰 Total Spending: ₹{total}")


def filter_by_category():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    search_category = input("Enter category to filter by: ")
    found_any = False

    print(f"\n----- Expenses in '{search_category}' -----")
    for expense in expenses:
        if expense['category'].lower() == search_category.lower():
            print(f"₹{expense['amount']} | {expense['description']}")
            found_any = True

    if not found_any:
        print("No expenses found in that category.")


def delete_expense():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    view_expenses()
    choice = input("Enter the number of the expense to delete: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(expenses):
        print("That number doesn't match any expense.")
        return

    removed = expenses.pop(index)
    save_expenses()
    print(f"Deleted: ₹{removed['amount']} | {removed['category']} | {removed['description']}")


load_expenses()

while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        filter_by_category()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")