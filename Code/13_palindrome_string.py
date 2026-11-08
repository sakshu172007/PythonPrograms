def is_palindrome_string(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return text == reversed_text


text = input("Enter a string: ")

print("Palindrome:", is_palindrome_string(text))


# python Code/13_palindrome_string.py