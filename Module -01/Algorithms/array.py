#GetEvents
def getOnlyEvens(numbers):
    result = []

    for i in range(len(numbers)):
        if i % 2 == 0 and numbers[i] % 2 == 0:
            result.append(numbers[i])

    print(result)


# Test 1
getOnlyEvens([1, 2, 3, 6, 4, 8])

# Test 2
getOnlyEvens([0, 1, 2, 3, 4])
