import csv
import os
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


def add_expense():
    category = input("Enter category: ")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Category", "Amount"])

        writer.writerow([category, amount])

    print("Expense saved successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    print("\nYour Expenses:")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            print(expense["Category"], "-", expense["Amount"])


def total_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            total += float(expense["Amount"])

    print("Total Expenses:", total)

def category_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n===== CATEGORY SUMMARY =====")

    for category, amount in categories.items():
        print(category, ":", amount)

def show_chart():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    categories = {}
    amounts = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    names = list(categories.keys())
    values = list(categories.values())

    plt.bar(names, values)
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expense by Category")

    plt.show()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Expense Chart")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        show_chart()

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")