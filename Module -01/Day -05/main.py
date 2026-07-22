#inheritance
class Account: 
    def __init__(self, owner, balance=0): 
        self.owner = owner 
        self.balance = balance 
    def deposit(self, amount): 
        self.balance += amount 
  
class SavingsAccount(Account):    # child inherits everything 
    pass 
  
s = SavingsAccount("Almaz", 1500) 
s.deposit(500)        # inherited method just works 
print(s.balance)      # 2000 


#super()reusing
class SavingsAccount(Account): 
    def __init__(self, owner, balance=0, rate=0.05): 
        super().__init__(owner, balance)   # parent setup 
        self.rate = rate                   # the extra 
    def add_interest(self): 
        self.deposit(self.balance * self.rate)  # reuse parent

#overriding
class Account: 
    def statement(self): 
        print(f"{self.owner}: {self.balance} ETB") 
  
class CurrentAccount(Account): 
    def statement(self):                 # override 
        print(f"[Current] {self.owner}: {self.balance} ETB") 

 #polymorphism
 accounts = [ 
    Account("Hanna", 1500), 
    SavingsAccount("Almaz", 1500), 
    CurrentAccount("Dawit", 800), 
] 
for acc in accounts: 
    acc.statement()       # the right version runs each time

#Ducktyping
def show_balance(item): 
    print(item.balance)    # only needs a .balance attribute 
  
show_balance(savings)      # works 
show_balance(wallet)       # works too, if it has .balance

#Abstraction
from abc import ABC, abstractmethod 
class Account(ABC): 
@abstractmethod 
def calculate_interest(self): 

#interfaces

class SavingsAccount(Account): 

def calculate_interest(self):    
 
   
   return self.balance * 0.05 
  
  class CurrentAccount(Account): 

 def calculate_interest(self):    

return 0    

# Inheritance 
class SavingsAccount(Account): 
    def add_interest(self): ... 
  
# Composition
class Account: 
    def __init__(self): 
        self.history = TransactionHistory()

