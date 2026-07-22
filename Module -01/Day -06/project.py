from abc import ABC, abstractmethod


class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_defaults()
        return cls._instance

    def _init_defaults(self):
        self.interest_rate = 0.05
        self.overdraft_limit = 1000

    def set_interest_rate(self, rate):
        self.interest_rate = rate

    def set_overdraft_limit(self, limit):
        self.overdraft_limit = limit


class AccountObserver(ABC):
    @abstractmethod
    def update(self, account, event, **data):
        ...


class SMSAlert(AccountObserver):
    def update(self, account, event, **data):
        message = data.get("message", event)
        print(f"[SMS to {account.owner}] {message}")


class AuditLog(AccountObserver):
    def __init__(self):
        self.entries = []

    def update(self, account, event, **data):
        entry = f"{account.account_number} | {event.upper()} | {data.get('message', '')}"
        self.entries.append(entry)
        print(f"[AUDIT] {entry}")

    def show(self):
        print("\n----- Audit Log -----")
        for entry in self.entries:
            print(entry)


class Account:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self._balance = 0
        self._observers = []

    @property
    def balance(self):
        return self._balance

    def subscribe(self, observer: AccountObserver):
        self._observers.append(observer)

    def _notify(self, event, **data):
        for observer in self._observers:
            observer.update(self, event, **data)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._notify("deposit", message=f"{amount} ETB deposited successfully.")
        else:
            self._notify("deposit_failed", message="Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            self._notify("withdraw_failed", message="Withdrawal amount must be greater than 0.")
        elif amount > self._balance:
            self._notify("withdraw_failed", message="Insufficient balance.")
        else:
            self._balance -= amount
            self._notify("withdraw", message=f"{amount} ETB withdrawn successfully.")

    def statement(self):
        print("\n----- Addis Bank Account Statement -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self._balance, "ETB")


class SavingsAccount(Account):
    def __init__(self, owner, account_number, rate=None):
        super().__init__(owner, account_number)
        self.rate = rate if rate is not None else BankConfig().interest_rate

    def add_interest(self):
        interest = self._balance * self.rate
        if interest > 0:
            self.deposit(interest)
            self._notify("interest", message=f"Interest added at {self.rate * 100:.1f}%.")
        else:
            self._notify("interest_skipped", message="No interest to add (zero or negative balance).")

    def statement(self):
        print("\n----- Addis Bank Savings Account Statement -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Interest Rate:", f"{self.rate * 100:.1f}%")
        print("Balance:", self._balance, "ETB")


class CurrentAccount(Account):
    def __init__(self, owner, account_number, overdraft_limit=None):
        super().__init__(owner, account_number)
        self.overdraft_limit = (
            overdraft_limit if overdraft_limit is not None else BankConfig().overdraft_limit
        )

    def withdraw(self, amount):
        if amount <= 0:
            self._notify("withdraw_failed", message="Withdrawal amount must be greater than 0.")
            return

        available = self._balance + self.overdraft_limit
        if amount > available:
            self._notify("withdraw_failed", message="Withdrawal exceeds overdraft limit.")
        else:
            self._balance -= amount
            self._notify("withdraw", message=f"{amount} ETB withdrawn successfully.")
            if self._balance < 0:
                self._notify("overdrawn", message=f"Account is overdrawn by {-self._balance} ETB.")

    def statement(self):
        print("\n----- Addis Bank Current Account Statement -----")
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Overdraft Limit:", self.overdraft_limit, "ETB")
        print("Balance:", self._balance, "ETB")


class AccountFactory:
    _account_types = {
        "savings": SavingsAccount,
        "current": CurrentAccount,
        "basic": Account,
    }

    @classmethod
    def create(cls, kind, owner, number, balance=0):
        account_cls = cls._account_types.get(kind.lower())
        if account_cls is None:
            raise ValueError(f"Unknown account type: {kind}")

        account = account_cls(owner, number)
        if balance > 0:
            account.deposit(balance)
        return account


if __name__ == "__main__":
    BankConfig().set_interest_rate(0.05)
    BankConfig().set_overdraft_limit(1000)

    sms = SMSAlert()
    audit = AuditLog()

    account1 = AccountFactory.create("basic", "Nahom Toti", "100200300")
    savings1 = AccountFactory.create("savings", "Nahom Toti", "200300400")
    current1 = AccountFactory.create("current", "Nahom Toti", "300400500")

    accounts = [account1, savings1, current1]
    for acc in accounts:
        acc.subscribe(sms)
        acc.subscribe(audit)

    account1.deposit(5000)
    account1.withdraw(1200)

    savings1.deposit(2000)
    savings1.add_interest()

    current1.deposit(500)
    current1.withdraw(1300)
    current1.withdraw(5000)

    print("\n========== Polymorphic Statement Loop ==========")
    for acc in accounts:
        acc.statement()

    print("\n========== Balances ==========")
    for acc in accounts:
        print(f"{acc.owner} ({type(acc).__name__}): {acc.balance} ETB")

    audit.show()