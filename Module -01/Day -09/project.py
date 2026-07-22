class Account:


    def __init__(self, owner, account_number):

        self.owner = owner
        self.account_number = account_number
        self._balance = 0
       self.history = []



    @property
    def balance(self):

        return self._balance




    def deposit(self, amount):

        if amount > 0:

            self._balance += amount

            self.history.append(
                ("deposit", amount)
            )

            print(
                f"{amount} ETB deposited successfully."
            )

        else:

            print(
                "Invalid deposit amount."
            )




    def withdraw(self, amount):

        if amount <= self._balance:

            self._balance -= amount

            self.history.append(
                ("withdraw", amount)
            )

            print(
                f"{amount} ETB withdrawn successfully."
            )


        else:

            print(
                "Insufficient balance."
            )




    def undo_last(self):

        if len(self.history) == 0:

            print(
                "No transaction found."
            )

            return



        action, amount = self.history.pop()



        if action == "deposit":

            self._balance -= amount



        elif action == "withdraw":

            self._balance += amount



        print(
            f"Undo completed: {action} {amount} ETB"
        )





    def statement(self):

        print(
            "\n----- Account Statement -----"
        )

        print(
            "Owner:",
            self.owner
        )

        print(
            "Account Number:",
            self.account_number
        )

        print(
            "Balance:",
            self.balance,
            "ETB"
        )



class SavingsAccount(Account):


    def __init__(self, owner, account_number):

        super().__init__(
            owner,
            account_number
        )

        self.interest_rate = 0.05




    def add_interest(self):

        interest = (
            self.balance *
            self.interest_rate
        )


        self.deposit(
            interest
        )




    def statement(self):

        print(
            "\n----- Savings Account -----"
        )

        print(
            "Owner:",
            self.owner
        )

        print(
            "Account Number:",
            self.account_number
        )

        print(
            "Interest Rate:",
            self.interest_rate
        )

        print(
            "Balance:",
            self.balance,
            "ETB"
        )


class CurrentAccount(Account):


    def __init__(self, owner, account_number):

        super().__init__(
            owner,
            account_number
        )

        self.overdraft_limit = 1000




    def withdraw(self, amount):

        available = (
            self.balance +
            self.overdraft_limit
        )


        if amount <= available:


            self._balance -= amount


            self.history.append(
                ("withdraw", amount)
            )


            print(
                f"{amount} ETB withdrawn successfully."
            )


        else:

            print(
                "Overdraft limit exceeded."
            )




    def statement(self):

        print(
            "\n----- Current Account -----"
        )

        print(
            "Owner:",
            self.owner
        )

        print(
            "Account Number:",
            self.account_number
        )

        print(
            "Overdraft:",
            self.overdraft_limit,
            "ETB"
        )

        print(
            "Balance:",
            self.balance,
            "ETB"
        )

class AccountRegistry:


    def __init__(self):

        self.accounts = {}

        self.order = []





    def add(self, account):

        self.accounts[
            account.account_number
        ] = account


        self.order.append(
            account
        )





    def find(self, account_number):

        return self.accounts.get(
            account_number
        )





    def list_all(self):

        return self.order






    # Top accounts by balance

    def top_by_balance(self, n):

        return sorted(
            self.order,
            key=lambda a: a.balance,
            reverse=True
        )[:n]






    # Binary search

    def binary_search(self, items, target):

        left = 0

        right = len(items)-1



        while left <= right:


            mid = (
                left + right
            ) // 2



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
            key=lambda a:a.account_number
        )


        return self.binary_search(
            sorted_accounts,
            number
        )
    def _recursive_sum(self, history, index):

        if index >= len(history):

            return 0



        return (
            history[index][1]
            +
            self._recursive_sum(
                history,
                index+1
            )
        )





    def total_transactions(self, number):

        account = self.find(number)


        if account is None:

            return 0



        return self._recursive_sum(
            account.history,
            0
        )


class AccountFactory:


    @staticmethod
    def create(kind, owner, number):


        if kind.lower() == "basic":

            return Account(
                owner,
                number
            )


        elif kind.lower() == "savings":

            return SavingsAccount(
                owner,
                number
            )


        elif kind.lower() == "current":

            return CurrentAccount(
                owner,
                number
            )


        else:

            raise ValueError(
                "Invalid account type."
            )
            


class Branch:


    def __init__(self, name):

        self.name = name

        self.children = []

        self.accounts = []





    def add_branch(self, branch):

        self.children.append(
            branch
        )





    def add_account(self, account):

        self.accounts.append(
            account
        )



    def total_balance(self):

        total = 0

        for account in self.accounts:

            total += account.balance 

        for child in self.children:

            total += child.total_balance()



        return total





    def display(self, level=0):

        print(
            "   " * level +
            self.name
        )


        for account in self.accounts:

            print(
                "   "*(level+1),
                account.owner,
                "-",
                account.balance,
                "ETB"
            )



        for child in self.children:

            child.display(
                level+1
            )



transfers = {

    "100200300":[
        "200300400",
        "300400500"
    ],


    "200300400":[
        "400500600"
    ],


    "300400500":[
        "400500600"
    ],


    "400500600":[]
}



from collections import deque



def bfs(transfers, start):


    visited = set()

    queue = deque()


    queue.append(
        start
    )


    result = []



    while queue:


        current = queue.popleft()



        if current not in visited:


            visited.add(
                current
            )


            result.append(
                current
            )



            for receiver in transfers.get(
                current,
                []
            ):

                queue.append(
                    receiver
                )



    return result
    


if __name__ == "__main__":



    # Create registry

    registry = AccountRegistry()



    # Create accounts

    account1 = AccountFactory.create(
        "basic",
        "Nahom Toti",
        "100200300"
    )


    savings1 = AccountFactory.create(
        "savings",
        "Abebe Kebede",
        "200300400"
    )


    current1 = AccountFactory.create(
        "current",
        "Sara Ali",
        "300400500"
    )


    account4 = AccountFactory.create(
        "basic",
        "Miki Tesfaye",
        "400500600"
    )




    # Add accounts to registry


    registry.add(account1)

    registry.add(savings1)

    registry.add(current1)

    registry.add(account4)





    # Transactions


    print("\n===== TRANSACTIONS =====")


    account1.deposit(
        5000
    )


    account1.withdraw(
        1200
    )



    savings1.deposit(
        3000
    )


    savings1.add_interest()



    current1.deposit(
        2000
    )


    current1.withdraw(
        2500
    )



    account4.deposit(
        1000
    )



    print(
        "\n===== ACCOUNT LIST ====="
    )


    for acc in registry.list_all():

        acc.statement()




    print(
        "\n===== TOP BALANCES ====="
    )


    for acc in registry.top_by_balance(3):

        print(
            acc.owner,
            "-",
            acc.balance,
            "ETB"
        )





    print(
        "\n===== BINARY SEARCH ====="
    )


    found = registry.find_by_number(
        "200300400"
    )


    if found:

        print(
            "Found:"
        )

        found.statement()




    print(
        "\n===== TOTAL TRANSACTIONS ====="
    )


    total = registry.total_transactions(
        "100200300"
    )


    print(
        "Total:",
        total,
        "ETB"
    )




    head_office = Branch(
        "Head Office"
    )


    east_region = Branch(
        "East Region"
    )


    west_region = Branch(
        "West Region"
    )



    addis_branch = Branch(
        "Addis Branch"
    )


    hawassa_branch = Branch(
        "Hawassa Branch"
    )


    bahir_branch = Branch(
        "Bahir Dar Branch"
    )





    # Build tree


    head_office.add_branch(
        east_region
    )


    head_office.add_branch(
        west_region
    )



    east_region.add_branch(
        addis_branch
    )


    east_region.add_branch(
        hawassa_branch
    )


    west_region.add_branch(
        bahir_branch
    )


    addis_branch.add_account(
        account1
    )


    hawassa_branch.add_account(
        savings1
    )


    bahir_branch.add_account(
        current1
    )


    west_region.add_account(
        account4
    )





    print(
        "\n===== BRANCH TREE ====="
    )


    head_office.display()





    print(
        "\nTOTAL BANK BALANCE:"
    )


    print(
        head_office.total_balance(),
        "ETB"
    )



    print(
        "\n===== TRANSFER GRAPH BFS ====="
    )



    reachable = bfs(
        transfers,
        "100200300"
    )


    print(
        "Reachable accounts:",
        reachable
    )