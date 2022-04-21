from unicodedata import name


class User:
    all_accounts = []
    def __init__(self, name, intBalance):
        self.name = name
        if intBalance > 0: 
            self.account_bal = intBalance
        else:
            self.account_bal = 0
        User.all_accounts.append(self)
    def display_user_balance(self):
        print(f"Hello {self.name}. Your balance is: ${self.account_bal}")
        return self
    def make_deposit(self, amount):
        self.account_bal += amount
        return self
    def make_withdrawal(self, amount):
        self.account_bal -= amount
        return self
    def yield_interest(self):
        if self.account_bal > 0:
            self.account_bal += self.account_bal*0.1 
            return self
    @classmethod
    def all_bal(cls):
        sum = 0
        for accounts in cls.all_accounts:
            sum += accounts.account_bal
        print(f"Everyone's money combined is: {sum}")

gary = User(name="Gary", intBalance=300)
jary = User(name="Jary", intBalance=0)

gary.make_deposit(300).make_deposit(300).make_deposit(300).make_withdrawal(20).yield_interest().display_user_balance()
jary.make_deposit(200).make_deposit(200).make_withdrawal(20).make_withdrawal(20).make_withdrawal(20).make_withdrawal(20).yield_interest().display_user_balance()
User.all_bal()

