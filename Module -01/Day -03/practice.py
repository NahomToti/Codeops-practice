#list of cities
cities = ["Addis Ababa", "Dire Dawa", "Mekelle", "Bahir Dar", "Gondar", "Hawassa"]
unique_cities = set(cities) 
print(unique_cities)
print(unique_cities)
print("Total unique cities:", len(unique_cities))


#price report
grocery_prices = {
    "bread": 20.50,
    "milk": 15.75,
     "eggs": 30.00,
    "cheese": 45.25,
    "vegetables": 25.00,
}
print("Grocery Price Report:")
for item, price in grocery_prices.items():
    print(f"{item}: {price} ETB")


#Tax comprehension
prices = [100, 250,  400, 80]
tax_prices = [price *1.15 for price in prices]
print("Prices with tax:", tax_prices)
print(tax_prices)



#cheap items
prices = [100, 250, 400, 80]
cheap_prices = [price for price in prices if price < 200]
print("Cheap items:", cheap_prices)
print(cheap_prices)


#write & read a file
with open("report.txt", "w") as file:
    file.write("Nahom\n")
    file.write("Selam\n")
    file.write("Bereket\n")

    with open("names.txt", "r") as file:
        print("Customer Names:")

        for name in file:
            print(name.strip())

# safe division
try:
    number= float(input("Enter a number: "))
    answer= 1000/number
    print("Result:", answer)

    except valueError:
    print("Invalid input! please enter a number.")
    except zeroDivisonError:
    print ("You cannot divide by zero .")    
    