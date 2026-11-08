def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(3) == 6

print("All test cases passed.")


# python Test_Code/test_04_factorial.py