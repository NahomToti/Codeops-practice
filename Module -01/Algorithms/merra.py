def checkMeera(numbers):
    for number in numbers:
        if number * 2 in numbers:
            print("I am NOT a Meera array")
            return

    print("I am a Meera array")


# Test 1
checkMeera([10, 4, 0, 5])

# Test 2
checkMeera([7, 4, 9])

# Test 3
checkMeera([1, -6, 4, -3])