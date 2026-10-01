# A class defines the data and behavior of an object.
# Use classes when state and related operations belong together.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"


account = BankAccount("Ada", 100)
account.deposit(50)
account.withdraw(20)
print(account)

# Each instance has independent state.
other_account = BankAccount("Grace")
print(other_account)
