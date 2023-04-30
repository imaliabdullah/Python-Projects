class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum([item["amount"] for item in self.ledger])

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Get total amount withdrawn from each category
    withdrawals = [sum([item["amount"] for item in category.ledger if item["amount"] < 0]) for category in categories]
    total_withdrawals = sum(withdrawals)
    # Calculate the percentage of the total withdrawals for each category
    percentages = [int(withdrawal / total_withdrawals * 10) * 10 for withdrawal in withdrawals]
    # Create the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    # Find the longest category name
    max_len = max([len(category.name) for category in categories])
    # Add the category names to the chart
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"
    return chart.rstrip()


food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
clothing.withdraw(25.55, "pants")
clothing.withdraw(100, "shirt")
auto.deposit(1000, "initial deposit")
auto.transfer(200, clothing)

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))