# DIP — depend on an abstraction, inject the detail 
class Account: 
def __init__(self, notifier: Notifier): 
self.notifier = notifier      # any Notifier works

#singleton
class BankConfig: 
    _instance = None 
    def __new__(cls): 
        if cls._instance is None: 
            cls._instance = super().__new__(cls) 
            cls._instance.interest_rate = 0.05 
            cls._instance.overdraft_limit = 1000 
        return cls._instance 
  
BankConfig() is BankConfig()    # True — same object 

#factory
class AccountFactory: 
    @staticmethod 
    def create(kind, owner, number, balance=0): 
        if kind == "savings": 
            return SavingsAccount(owner, number, balance) 
        if kind == "current": 
            return CurrentAccount(owner, number, balance) 
        raise ValueError(f"Unknown type: {kind}") 
  
acc = AccountFactory.create("savings", "Almaz", "CBE-1", 1500)

#observer
class Account: 
    def __init__(self): 
        self._observers = [] 
    def subscribe(self, obs): 
        self._observers.append(obs) 
    def _notify(self, event): 
        for obs in self._observers: 
            obs.update(event) 
    def withdraw(self, amount): 
        self.balance -= amount 
        self._notify(f"-{amount} ETB")
     class SMSAlert: 
    def update(self, event): 
        print(f"[TeleBirr SMS] {event}") 
  
class AuditLog: 
    def update(self, event): 
        print(f"[Log] {event}") 
  
acc.subscribe(SMSAlert()) 
acc.subscribe(AuditLog()) 
acc.withdraw(5000)        # both observers fire


