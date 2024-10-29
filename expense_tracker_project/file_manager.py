import json

def load_expenses(file_path="expenses.txt"):
    try:
        with open(file_path, "r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        return []

def save_expenses(expenses, file_path="expenses.txt"):
    with open(file_path, "w") as file:
        json.dump(expenses, file)
