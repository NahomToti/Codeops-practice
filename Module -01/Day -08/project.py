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


    def top_by_balance(self, n):
        return sorted(
            self.order,
            key=lambda a: a.balance,
            reverse=True
        )[:n]



    def binary_search(self, items, target):
        left = 0
        right = len(items) - 1

        while left <= right:
            mid = (left + right) // 2

            if items[mid].account_number == target:
                return items[mid]
            elif items[mid].account_number < target:
                left = mid + 1
            else:
                right = mid - 1

        return None
    def find_by_number(self, number):
        sorted_accounts = sorted(
            self.order,
            key=lambda a: a.account_number
        )
        return self.binary_search(sorted_accounts, number)


    def _recursive_sum(self, history, index):
        if index >= len(history):
            return 0

        return history[index][1] + self._recursive_sum(history, index + 1)


    def total_transactions(self, number):
        account = self.find(number)

        if account is None:
            return 0

        return self._recursive_sum(account.history, 0)


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


if __name__ == "__main__":

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
        print(f"{acc.owner} ({type(acc).__name__}) : {acc.balance} ETB")

    print("\n= Find Account =")
    account = registry.find("200300400")
    if account:
        account.statement()

    print("\n= Undo Last Transaction =")
    account1.undo_last()
    account1.statement()
    audit.show()



    print("\n= TOP BALANCES =")
    for acc in registry.top_by_balance(3):
        print(f"{acc.owner} ({type(acc).__name__}) - {acc.balance} ETB")

    print("\n= BINARY SEARCH =")
    found = registry.find_by_number("200300400")

    if found:
        print("Account Found:")
        found.statement()
    else:
        print("Account not found.")

    print("\n= TOTAL TRANSACTIONS =")
    total = registry.total_transactions("100200300")
    print("Total transaction amount:", total, "ETB")