#1Temperature Label

temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 15:
    print("Cold")
elif temperature <= 28:
    print("Warm")
else:
    print("Hot")


#2Receipt loop
print("\nReceipt Numbers:")

for number in range(1, 11):
    print(f"Receipt #{number}")

#3Even or Odd
print("\nEven numbers")
for number in range(1, 21):
    if number % 2 == 0:
        print(number)



#3 Discount function
def apply_discount(price, percent=10):
    discount = price * (percent / 100)
    final_price = price - discount
    return final_price
# Test the function
print("\nDiscount Function:")

print("Price after default 10% discount:", apply_discount(100))
print("Price after 20% discount:", apply_discount(100, 20))


# countdown
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
    print("Liftoff!")