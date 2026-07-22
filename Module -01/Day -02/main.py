#Data Types
student_name = "Almaz Bekele"  #str
age = 24                       #int 
balance = 1500.50              #float 
is_enrolled = True             #bool 
verified = None                #NoneType


#conversion
age_text = input("Your age: ")   # e.g. "24" (a string!) 
age = int(age_text)              # 24  (now an int) 
next_year = age + 1              # works only after int() 


#comparison logical
balance = 1500      # ETB 
is_member = True    
  balance == 1500            # True 
balance > 1000 and is_member   # True 
not is_member                  # False 


#control flow
balance = 1500   # ETB 
  
if balance >= 1000: 
    print("Premium customer") 
elif balance >= 500: 
    print("Standard customer") 
else: 
    print("Basic customer")

# while loop 
count = 3 
while count > 0: 
print(f"Sending... {count}") 
count = count - 1  # for — walk a range or a list 
for i in range(1, 4):        
print(f"Receipt #{i}")  # 1, 2, 3 (stops before 4) 
for name in ["Almaz", "Dawit", "Tigist"]: 
print(f"Selam, {name}")


#functions
def add_tax(price, rate=0.15): 
return price + price * rate 
total = add_tax(1000)            # 1150.0  (uses default rate) 
total = add_tax(1000, rate=0.10) # 1100.0  (keyword argument)

#variable scope
tax_rate = 0.15        # global — readable anywhere 
def total(price): 
fee = 50            # local — exists only in here 
return price + fee 
print(total(1000))   # 1050     
print(tax_rate)      # 0.15   (ok — global)   
print(fee)          # NameError — fee is local! 