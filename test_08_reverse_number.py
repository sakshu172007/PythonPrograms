def reverse_number(number):
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return reversed_number


assert reverse_number(12345) == 54321
assert reverse_number(123) == 321
assert reverse_number(100) == 1
assert reverse_number(5) == 5
assert reverse_number(9876) == 6789

print("All test cases passed.")


# python Test_Code/test_08_reverse_number.py