def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return original_number == reversed_number


number = int(input("Enter a number: "))

print("Palindrome:", is_palindrome(number))


# python Code/09_palindrome_number.py