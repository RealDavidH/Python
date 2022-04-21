
class User:
    def __init__(self, name, email_address, intBalance, accountName):
        self.name = name
        self.email = email_address
        
        self.account = Bank_account(intBalance, accountName)
        
        if len(Bank_account.user_accounts) == 0:
            Bank_account.user_accounts[accountName] = intBalance
        
        
    def open_account(self, accountName, amount):
        pass
        Bank_account.user_accounts[accountName] = amount
        return self

    def make_deposit(self, amount, accountName):
        self.account.make_deposit(amount, accountName)
        return self
    
    def make_withdrawal(self, amount, accountName):
        self.account.make_withdrawal(amount, accountName)
        return self
    
    def transfer(self, other_user, amount, accountName):
        self.account -= amount
        other_user.account += amount
        return self
    
    def display_user_balance(self, accountName):
        print(f"Hello {self.name}. Your balance for {accountName} is: ${self.account.account_bal}")
        return 
    
    def display_user_accounts(self):
        print(Bank_account.user_accounts)
    


class Bank_account:
    all_accounts = []
    user_accounts = {
        
    }
    
    def __init__(self, intBalance, accountName):
        if intBalance > 0: 
            self.account_bal = intBalance
        else:
            self.account_bal = 0
        self.account_name = accountName
        
        Bank_account.all_accounts.append(self)
        
    def make_deposit(self, amount, account_num):
        print("What account would you like to deposit into?")
        account_num = input()
        int(account_num)
        if account_num == 1:
            key = Bank_account.user_accounts[0]
            self.account_bal = key[0]
            print(key[0])
            int(self.account_bal)
            self.account_bal += amount
        return self
    def make_withdrawal(self, amount, account_name):
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



greg = User(name="Greg Smelly",email_address="gsmelly@gmail.com", intBalance=300, accountName="account1")

greg.open_account("account2", amount=300)
greg.make_deposit(amount=300, accountName="account1")
greg.display_user_balance("account1")
greg.display_user_accounts()



