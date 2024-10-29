class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        """Add a new expense with amount, category, and description."""
        expense = {"amount": amount, "category": category, "description": description}
        self.expenses.append(expense)

    def list_expenses(self):
        """Return the list of all expenses."""
        return self.expenses

    def get_summary(self):
        """Return a summary of expenses by category."""
        summary = {}
        for expense in self.expenses:
            category = expense["category"]
            amount = expense["amount"]
            summary[category] = summary.get(category, 0) + amount
        return summary
