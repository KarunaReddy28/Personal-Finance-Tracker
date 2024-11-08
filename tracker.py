class Tracker:
    def __init__(self):
        self.income = []
        self.expenses = []

    def add_income(self, amount, description):
        self.income.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def calculate_balance(self):
        total_income = sum(item['amount'] for item in self.income)
        total_expense = sum(item['amount'] for item in self.expenses)
        return total_income - total_expense
