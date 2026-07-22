# read one line at a time 
with open("customers.txt") as f: 
    for line in f: 
        print(line.strip())   # strip() trims the newline 
  
# read the whole file into one string 
with open("customers.txt") as f: 
    text = f.read() 


  #writing a file
   with open("report.txt", "w") as f:    # "w" overwrites 
    f.write("Daily Report\n") 
    f.write("Total: 1500 ETB\n") 
  
with open("log.txt", "a") as f:       # "a" appends 
    f.write("New entry\n") 

 #Exception handling
  try: 
amount = int(input("Amount: ")) 
result = 1000 / amount 
except ValueError: 
print("Please enter a number") 
except ZeroDivisionError: 
print("Amount can't be zero") 
else: 
print(result)   # runs only if no error 
finally: 
print("Done")   # always runs 

