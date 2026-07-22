#List index
numbers =[10, 20, 30, 40, 50]
print(numbers[2])

#single loop
numbers =[10, 20, 30, 40, 50]
for num in numbers:
    print(num)

    # nested loop
    numbers =[1,2,3]
    for i in numbers:
        for j in numbers:
            print(i,j)

# Dictionary lookup
student ={
    "101":"Nahom",
    "102":"Feven",
    "103":"edom",
}
print(students["102"])

# Binary Search 

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


numbers = [5, 10, 15, 20, 25, 30, 35]

print(binary_search(numbers, 20))


#list vs Dictionary lookup
import time


account_list = list(range(100000))


account_dict = {}

for number in range(100000):
    account_dict[number] = f"Account {number}"

target = 99999

# List lookup
start = time.time()

target in account_list

end = time.time()

print("List lookup time:", end - start)

# Dictionary lookup
start = time.time()

target in account_dict

end = time.time()

print("Dictionary lookup time:", end - start)

#building stack
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


stack = Stack()

names = ["Nahom", "Feven", "Samuel", "Abel"]


for name in names:
    stack.push(name)

print("Top Item:", stack.peek())

print("Names in Reverse:")

while len(stack.items) > 0:
    print(stack.pop())