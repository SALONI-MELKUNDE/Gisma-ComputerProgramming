class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance


account = BankAccount(1000)


account.deposit(500)


account.withdraw(300)


account.withdraw(2000)


current_balance = account.get_balance()


print(f"Current Balance: {current_balance}")

