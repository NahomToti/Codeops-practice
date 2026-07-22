# Book class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"'{self.title}' by {self.author} has {self.pages} pages.")


# Create two books
book1 = Book("Python Basics", "John Smith", 250)
book2 = Book("Learning AI", "Sara Johnson", 320)

# Display information
book1.describe()
book2.describe()


# Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        self.quantity -= n



product = Product("Sugar", 90, 20)

print("Quantity:", product.quantity)

product.restock(10)
print("After restocking:", product.quantity)

product.sell(5)
print("After selling:", product.quantity)



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        self.__quantity -= n



product = Product("Rice", 150, 30)

print("Quantity:", product.quantity)
# Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        if n <= self.__quantity:
            self.__quantity -= n
        else:
            print("Not enough stock available.")


# Validate product
product = Product("Milk", 80, 10)

product.sell(4)
print("Quantity:", product.quantity)

product.sell(10)
print("Quantity:", product.quantity)

class Product:

    def __init__(self, name, price, quantity):

        self.name = name

        self.price = price

        self.__quantity = quantity

    @property

    def quantity(self):

        return self.__quantity

    def restock(self, n):

        self.__quantity += n

    def sell(self, n):

        if n <= self.__quantity:

            self.__quantity -= n

        else:

            print("Not enough stock available.")



product = Product("Milk", 80, 10)

product.sell(4)

print("Quantity:", product.quantity)

product.sell(10)

print("Quantity:", product.quantity)
class Product:

    def __init__(self, name, price, quantity):

        self.name = name

        self.price = price

        self.__quantity = quantity

    @property

    def quantity(self):

        return self.__quantity

    def restock(self, n):

        self.__quantity += n

    def sell(self, n):

        if n <= self.__quantity:

            self.__quantity -= n

        else:

            print("Not enough stock.")



product1 = Product("Bread", 50, 20)

product2 = Product("Rice", 150, 30)

product3 = Product("Oil", 350, 15)



product1.sell(5)



print("Bread Quantity:", product1.quantity)

print("Rice Quantity:", product2.quantity)

print("Oil Quantity:", product3.quantity)