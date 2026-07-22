self._notify(
                "interest",
                message=f"Interest added ({self.rate*100:.1f}%)."
            )

    def statement(self):

        print("\n----- Savings Account -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Interest Rate:", self.rate)
        print("Balance:", self.balance, "ETB")



class CurrentAccount(Account):

    def __init__(self, owner, account_number, overdraft=None):

        super().__init__(owner, account_number)

        if overdraft is None:
            self.overdraft_limit = BankConfig().overdraft_limit
        else:
            self.overdraft_limit = overdraft

    def withdraw(self, amount):

        if amount <= 0:

            self._notify(
                "withdraw_failed",
                message="Withdrawal amount must be greater than 0."
            )
            return

        available = self._balance + self.overdraft_limit

        if amount > available:

            self._notify(
                "withdraw_failed",
                message="Withdrawal exceeds overdraft limit."
            )

        else:

            self._balance -= amount

            self.history.append(("withdraw", amount))

            self._notify(
                "withdraw",
                message=f"{amount} ETB withdrawn successfully."
            )

            if self._balance < 0:

                self._notify(
                    "overdrawn",
                    message=f"Account overdrawn by {-self._balance} ETB."
                )

    def statement(self):

        print("\n----- Current Account -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Overdraft:", self.overdraft_limit, "ETB")
        print("Balance:", self.balance, "ETB")



class AccountRegistry:

    def __init__(self):
        self.accounts = {}
        self.order = []

    
    def add(self, account):

        self.accounts[account.account_number] = account
        self.order.append(account)

    
    def find(self, account_number):

        return self.accounts.get(account_number)

    def list_all(self):

        return self.order



class AccountFactory:

    @staticmethod
    def create(kind, owner, number):

        if kind.lower() == "basic":
            return Account(owner, number)

        elif kind.lower() == "savings":
            return SavingsAccount(owner, number)

        elif kind.lower() == "current":
            return CurrentAccount(owner, number)

        else:
            raise ValueError("Invalid account type.")

if name == "__main__":

    
    config = BankConfig()
    config.set_interest_rate(0.05)
    config.set_overdraft_limit(1000)

    
    sms = SMSAlert()
    audit = AuditLog()

    
    registry = AccountRegistry()

    
    account1 = AccountFactory.create(
        "basic",
        "Nahom Toti",
        "100200300"
    )

    savings1 = AccountFactory.create(
        "savings",
        "Nahom Toti",
        "200300400"
    )

    current1 = AccountFactory.create(
        "current",
        "Nahom Toti",
        "300400500"
    )

    
    registry.add(account1)
    registry.add(savings1)
    registry.add(current1)

    
    for acc in registry.list_all():
        acc.subscribe(sms)
        acc.subscribe(audit)


    print("\n= Basic Account =")

    account1.deposit(5000)
    account1.withdraw(1200)

    
    print("\n= Savings Account =")

    savings1.deposit(2000)
    savings1.add_interest()


    print("\n= Current Account =")

    current1.deposit(500)

    
    current1.withdraw(1300)

    
    current1.withdraw(5000)

  
    print("\n= Account Statements =")

    for acc in registry.list_all():
        acc.statement()

    
    print("\n= Account Balances =")

    for acc in registry.list_all():
        print(
            f"{acc.owner} ({type(acc).__name__}) : {acc.balance} ETB"
        )

    
    print("\n= Find Account =")

    account = registry.find("200300400")

    if account:
        account.statement()

    print("\n========== Undo Last Transaction ==========")

    account1.undo_last()
    account1.statement()
    audit.show()

