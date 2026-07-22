
def total(nums):
    ""Recursively returns the sum of a list.""
    if not nums:
        return 0
    return nums[0] + total(nums[1:])


def count_down(n):
    ""Recursively prints numbers from n down to 1.""
    if n <= 0:
        return
    print(n)
    count_down(n - 1)


print("1. Recursive Sum")
numbers = [10, 20, 30, 40]
print("Sum:", total(numbers))

print("\nCountdown:")
count_down(5)




def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print("\n2. Binary Search")
balances = [100, 250, 400, 600, 750, 900]
print("Index of 600:", binary_search(balances, 600))
print("Index of 500:", binary_search(balances, 500))



def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


print("\n3. Merge Sort")
nums = [8, 3, 1, 6, 7, 2, 5, 4]
sorted_nums = merge_sort(nums)

print("Original:", nums)
print("Merge Sorted:", sorted_nums)
print("Matches sorted():", sorted_nums == sorted(nums))




accounts = [
    ("Alice", 2500),
    ("Bob", 1800),
    ("Charlie", 3200),
    ("David", 2900),
]

sorted_accounts = sorted(accounts, key=lambda x: x[1], reverse=True)

print("\n4. Sort by Balance (Descending)")
for name, balance in sorted_accounts:
    print(name, balance)




def has_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return True
        elif current < target:
            left += 1
        else:
            right -= 1

    return False


print("\n5. Two Pointers")
numbers = [1, 2, 3, 4, 6, 8, 10]

print("Target 10:", has_pair(numbers, 10))
print("Target 15:", has_pair(numbers, 15))