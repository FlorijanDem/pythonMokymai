class BankAccount:
    def __init__(self, name: str, account: str):
        self.name = name
        self.account = account
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Not enough funds.")

    def get_balance(self):
        return self._balance

    def display_info(self):
        return f"Name: {self.name}, Account: {self.account}, Balance: {self._balance}"


class SavingAccount(BankAccount):
    def __init__(self, name, account, interest_rate):
        super().__init__(name, account)
        self.interest_rate = interest_rate  # Annual interest in %

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)


class CreditAccount(BankAccount):
    def __init__(self, name, account, credit_limit):
        super().__init__(name, account)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        # Balance may go negative up to the credit limit
        if self.get_balance() - amount >= -self.credit_limit:
            self._balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Credit limit exceeded.")


# Create accounts
jonas = BankAccount("Jonas Jonaitis", "LT554555")
artur = SavingAccount("Artur Arturaitis", "LT1112", 3)
agne = CreditAccount("Agne Agnaite", "LT7777", 500)

# Test BankAccount
jonas.deposit(1000)
jonas.withdraw(250)
print(jonas.display_info())

print()

# Test SavingAccount
artur.deposit(2000)
artur.apply_interest()
print(artur.display_info())

print()

# Test CreditAccount
agne.withdraw(300)
print(agne.display_info())

agne.withdraw(300)
print(agne.display_info())

agne.withdraw(100)
print(agne.display_info())