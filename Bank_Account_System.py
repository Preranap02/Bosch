class Bank_Account_System:
    def __init__(self, username, account_number):
        self.username = username
        self.account_number = account_number
        self.balance = 0.0
 
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"
 
    def show_balance(self):
        return f"Current Balance: {self.balance}"
 
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
 
    def account_details(self):
        return (f"Account Holder: {self.username}\n"
                f"Account Number: {self.account_number}\n"
                f"{self.show_balance()}")
 
class SavingsAccount(Bank_Account_System):
    def __init__(self, username, account_number, interest_rate):
        super().__init__(username, account_number)
        self.interest_rate = interest_rate
 
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return f"Interest applied. New balance: {self.balance}"
 
class CurrentAccount(Bank_Account_System):
    def __init__(self, username, account_number, overdraft_limit):
        super().__init__(username, account_number)
        self.overdraft_limit = overdraft_limit
        self.balance = 0
 
    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            return "Overdraft_Limit exceeded"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
 
if __name__ == "__main__":
    username = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
 
    account1 = Bank_Account_System(username, account_number)
    print(account1.account_details())
    print(account1.deposit(10000))
    print(account1.withdraw(1500))
    print(account1.show_balance())
 
    savings_username = input("Enter savings account holder name: ")
    savings_account_number = input("Enter savings account number: ")
    savings = SavingsAccount(savings_username, savings_account_number, 5)
    print(savings.account_details())
    print(savings.deposit(5000))
    print(savings.apply_interest())
    print(savings.show_balance())
 
    current_username = input("Enter current account holder name: ")
    current_account_number = input("Enter current account number: ")
    current = CurrentAccount(current_username, current_account_number, 200)
    print(current.account_details())
    print(current.deposit(1000))
    print(current.withdraw(1100)) 
    print(current.show_balance())
    print(current.withdraw(300)) 
    print(current.show_balance())
 
 