#classAccount
 
 def __init__(self, owner, balance): 

self.owner = owner        # store data on the object 

self.balance = balance 

almaz = Account("Almaz", 1500)   # __init__ runs, self = almaz 

print(almaz.owner)               # Almaz


#Attributes & methods
class Account: 

def __init__(self, owner, balance): 

self.owner = owner 

self.balance = balance 

def deposit(self, amount):       # a method 

self.balance += amount 

def statement(self): 

print(f"{self.owner}: {self.balance} ETB") 

almaz = Account("Almaz", 1500) 

almaz.deposit(500)        # call a method with dot notation 

almaz.statement()         # Almaz: 2000 ETB

#Getter, setter & validation

class Account: 

def __init__(self, balance): 

  self.__balance = balance        # private 

   def withdraw(self, amount): 

    if amount > self.__balance: 

     print("Insufficient funds") 

     return 

     self.__balance -= amount 

     #properties

     class Account: 
def __init__(self, balance): 

self.__balance = balance 

  @property 

def balance(self):              # getter 
 
  return self.__balance 

   @balance.setter 
  
  def balance(self, value):       
   
   if value < 0: 

    raise ValueError("No negative balance") 

   self.__balance = value 

    a = Account(1500)
     a.balance         # setter with validation  # 1500   (runs the getter) 
   
   a.balance = 2000   # ok     

   (runs the setter) 

   a.balance = -5     # ValueError 


   