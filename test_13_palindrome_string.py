def is_palindrome(text):
    return text == text[::-1]


assert is_palindrome("madam") == True
assert is_palindrome("level") == True
assert is_palindrome("hello") == False
assert is_palindrome("python") == False
assert is_palindrome("racecar") == True

print("All test cases passed.")


# python Test_Code/test_13_palindrome_string.py