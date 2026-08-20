class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

account = BankAccount(10000)

account.deposit(5000)
account.withdraw(13000)
print(account.balance)