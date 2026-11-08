def sum_of_digits(number):
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    return total


assert sum_of_digits(12345) == 15
assert sum_of_digits(123) == 6
assert sum_of_digits(100) == 1
assert sum_of_digits(9) == 9
assert sum_of_digits(567) == 18

print("All test cases passed.")


# python Test_Code/test_10_sum_of_digits.py