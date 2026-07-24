def reverseCompare(number):
    reversed_number = int(str(number)[::-1])

    if number > reversed_number:
        print("Ok")
    else:
        print("Not ok")


# Test 1
reverseCompare(72)

# Test 2
reverseCompare(23)