class Category:


    def __init__(self, name):
        self.name = name
        self.amounts = []
        self.amount = 0
        self.description = ''
        self.ledger = []
        self.entry = {}
        self.balance = float()

    def __str__(self):
        output = ''''''
        output = output + self.name.center(30,"*") + "\n"
        for x in self.ledger:
            output = output + str(x["description"])[:23].ljust(23) + "{:.2f}".format(x["amount"]).rjust(7)+ "\n"

        return output

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount":amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.deposit(amount * -1, description)
            return True
        else:
            return False

    def get_balance(self):
        self.amounts = []
        for self.entry in self.ledger:
            self.amounts.append(self.entry["amount"])
        return sum(self.amounts)

    def check_funds(self,amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def transfer(self, amount, cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + cat.name)
            cat.deposit (amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def show_ledger(self):
        for x in self.ledger:
            print(x)


def create_spend_chart(categories):
    table_dat = []
    g_total = 0.0
    output = ''''''
    output = output + "Percentage spent by category\n"
    col_cnt = len(categories)
    for cat in categories:
        total = 0.0
        for item in cat.ledger:
            if "deposit" not in item["description"] and "Transfer" not in item["description"]:
                total = total + abs(item["amount"])
        g_total += total
        table_dat.append([cat.name, total])
    for item in table_dat:
        item[1] = "oooooooooo"[:int((10 * (item[1]  ) // g_total))]
    print(table_dat, '\n', g_total)


    return output
    # Percentage spent by category
    # 100|
    #  90|
    #  80|
    #  70|
    #  60| o
    #  50| o
    #  40| o
    #  30| o
    #  20| o  o
    #  10| o  o  o
    #   0| o  o  o
    #     ----------
    #      F  C  A
    #      o  l  u
    #      o  o  t
    #      d  t  o
    #         h
    #         i
    #         n
    #         g








food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))