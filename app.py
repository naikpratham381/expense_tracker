from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        save_expenses()
        return redirect(url_for("home"))

    return render_template("add_expense.html")

@app.route("/view-expenses")
def view_expenses():
    return render_template("view_expenses.html", expenses=expenses)

@app.route("/total-spending")
def total_spending():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]

    return render_template("total_spending.html", total=total)

@app.route("/filter")
def filter_by_category():
    search_category = request.args.get("category", "")
    filtered = []

    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            filtered.append(expense)

    return render_template("filter.html", expenses=filtered, search_category=search_category)

load_expenses()

if __name__ == "__main__":
    app.run(debug=True)