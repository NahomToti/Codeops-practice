# Addis Bank - Account Management System

class Account:
    
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.__balance = 0

    
    @property
    def balance(self):
        return self.__balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} ETB deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount} ETB withdrawn successfully.")

    
    def statement(self):
        print("\n----- Addis Bank Account Statement -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance, "ETB")


# Create an account
account1 = Account("Nahom Toti", "100200300")


account1.statement()


account1.deposit(5000)


account1.withdraw(1200)


account1.deposit(-100)


account1.withdraw(10000)


account1.statement()


print("\nCurrent Balance:", account1.balance, "ETB")