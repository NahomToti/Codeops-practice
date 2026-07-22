# Addis Bank - Account Management System extended

class Account:

    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} ETB deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print(f"{amount} ETB withdrawn successfully.")

    def statement(self):
        print("\n----- Addis Bank Account Statement -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self._balance, "ETB")


class SavingsAccount(Account):
    ""Earns interest on the current balance.""

    def __init__(self, owner, account_number, rate):
        super().__init__(owner, account_number)
        self.rate = rate  

    def add_interest(self):
        
        interest = self._balance * self.rate
        if interest > 0:
            print(f"Adding interest at {self.rate * 100:.1f}% ...")
            self.deposit(interest)
        else:
            print("No interest to add (zero or negative balance).")

    def statement(self):
        print("\n----- Addis Bank Savings Account Statement -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Interest Rate:", f"{self.rate * 100:.1f}%")
        print("Balance:", self._balance, "ETB")


class CurrentAccount(Account):
    ""Allows withdrawals to go negative, down to an overdraft limit.""

    def __init__(self, owner, account_number, overdraft_limit):
        super().__init__(owner, account_number)
        self.overdraft_limit = overdraft_limit  # e.g. 1000 ETB allowed below 0

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        
        available = self._balance + self.overdraft_limit

        if amount > available:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self._balance -= amount
            print(f"{amount} ETB withdrawn successfully.")
            if self._balance < 0:
                print(f"Account is overdrawn by {-self._balance} ETB.")

    def statement(self):
        print("\n----- Addis Bank Current Account Statement -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Overdraft Limit:", self.overdraft_limit, "ETB")
        print("Balance:", self._balance, "ETB")




if __name__ == "__main__":
    account1 = Account("Nahom Toti", "100200300")
    savings1 = SavingsAccount("Nahom Toti", "200300400", rate=0.05)
    current1 = CurrentAccount("Nahom Toti", "300400500", overdraft_limit=1000)

    accounts = [account1, savings1, current1]

    
    account1.deposit(5000)
    account1.withdraw(1200)

    savings1.deposit(2000)
    savings1.add_interest()

    current1.deposit(500)
    current1.withdraw(1300)  # goes into overdraft
    current1.withdraw(5000)  # exceeds overdraft limit -> rejected

    print("\n========== Polymorphic Statement Loop ==========")
    for acc in accounts:
        acc.statement()

    print("\n========== Balances ==========")
    for acc in accounts:
        print(f"{acc.owner} ({type(acc).__name__}): {acc.balance} ETB")