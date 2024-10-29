from expense_manager import ExpenseManager
import file_manager

def display_expenses(expense_manager):
    expenses = expense_manager.list_expenses()
    if not expenses:
        print("No expenses recorded!")
        return
    print("\nList of Expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. ${expense['amount']} - {expense['category']} - {expense['description']}")

def display_summary(expense_manager):
    summary = expense_manager.get_summary()
    if not summary:
        print("No expenses recorded!")
        return
    print("\nExpense Summary by Category:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

def main():
    expense_manager = ExpenseManager()
    expense_manager.expenses = file_manager.load_expenses()  # Load existing expenses

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. View summary by category")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Transport): ")
            description = input("Enter description: ")
            expense_manager.add_expense(amount, category, description)
            file_manager.save_expenses(expense_manager.expenses)
            print("Expense added successfully!")
        elif choice == "2":
            display_expenses(expense_manager)
        elif choice == "3":
            display_summary(expense_manager)
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
