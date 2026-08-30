from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

FILE_NAME = "expenses.csv"


def get_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                expenses.append(expense)

    return expenses


@app.route("/")
def home():
    expenses = get_expenses()

    total = 0

    for expense in expenses:
        total += float(expense["Amount"])

    categories = {}

    for expense in expenses:
        category = expense["Category"]
        amount = float(expense["Amount"])

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        categories=categories
    )


@app.route("/add", methods=["POST"])
def add_expense():
    category = request.form["category"]
    amount = float(request.form["amount"])

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Category", "Amount"])

        writer.writerow([category, amount])

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)