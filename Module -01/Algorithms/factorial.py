def returnFactorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


# Test 1
print(returnFactorial(5))

# Test 2
print(returnFactorial(6))

# Test 3
print(returnFactorial(0))