def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return original_number == reversed_number


assert is_palindrome(121) == True
assert is_palindrome(12321) == True
assert is_palindrome(123) == False
assert is_palindrome(10) == False
assert is_palindrome(7) == True

print("All test cases passed.")


# python Test_Code/test_09_palindrome_number.py