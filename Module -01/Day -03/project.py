#pharamacy Inventory Tracker
try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, quantity = line.strip().split(",")
            stock[item] = int(quantity)

      except FileNotFoundError:
        print("stock.txt was not found.")
        print("A new stock File will be created.")

        def update_stock(item, amount):
            if item in stock:
                stock[item] += amount
                else:
                stock[item] = amount

     print("\ncurrent stock")
     for item, quantity in stock.items():
        
        print(item_name, change)
        
        update_stock(item_name, change)
        
        print("/nupdated stock")
        
        for item, quantity in stock.items():
        
        print(item, "-", quantity)
        

        print("\nLow Stock Items (Less than 10)")

    low_stock = [item for item, quantity in stock.items() if quantity < 10]

if low_stock:

    for item in low_stock:

        print(item, "-", stock[item])

else:

    print("No low-stock items.")

with open("stock.txt", "w") as file:

    for item, quantity in stock.items():

        file.write(f"{item},{quantity}\n")

print("\nStock has been saved successfully.")