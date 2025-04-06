import json
import datetime

def load_expenses(filename="expenses.json"):
    """Loads expenses from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses, filename="expenses.json"):
    """Saves expenses to a JSON file."""
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    """Adds a new expense."""
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = datetime.date.today().strftime("%Y-%m-%d") # Today's date in YYYY-MM-DD format.
    description = input("Enter description (optional): ")

    new_expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description,
    }
    expenses.append(new_expense)
    print("Expense added successfully!")
    return expenses

def view_expenses(expenses):
    """Views all expenses."""
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expenses ---")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']},"
              f" Description: {expense['description']}")
    print("-----------------\n")

def view_expenses_by_category(expenses):
    """Views expenses by category."""
    if not expenses:
        print("No expenses recorded.")
        return

    category = input("Enter category to view: ")
    filtered_expenses = [expense for expense in expenses if expense["category"].lower() == category.lower()]

    if not filtered_expenses:
        print(f"No expenses found for category: {category}")
        return

    print(f"\n--- Expenses for Category: {category} ---")
    for i, expense in enumerate(filtered_expenses):
        print(f"{i+1}. Date: {expense['date']}, Amount: ${expense['amount']}, Description: {expense['description']}")
    print("-----------------\n")

def view_expenses_by_date(expenses):
    """View expenses by date."""

    if not expenses:
        print("No expenses recorded.")
        return

    date_input = input("Enter date (YYYY-MM-DD): ")
    filtered_expenses = [expense for expense in expenses if expense["date"] == date_input]

    if not filtered_expenses:
        print(f"No expenses found for date: {date_input}")
        return

    print(f"\n--- Expenses for Date: {date_input} ---")
    for i, expense in enumerate(filtered_expenses):
        print(f"{i+1}. Category: {expense['category']}, Amount: ${expense['amount']}, Description: {expense['description']}")
    print("-----------------\n")

def main():
    """Main function to run the expense tracker."""
    expenses = load_expenses()

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expenses by Category")
        print("4. View Expenses by Date")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            expenses = add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_expenses_by_category(expenses)
        elif choice == "4":
            view_expenses_by_date(expenses)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()