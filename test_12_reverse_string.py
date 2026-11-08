def reverse_string(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return reversed_text


assert reverse_string("hello") == "olleh"
assert reverse_string("Python") == "nohtyP"
assert reverse_string("12345") == "54321"
assert reverse_string("abc") == "cba"
assert reverse_string("madam") == "madam"

print("All test cases passed.")


# python Test_Code/test_12_reverse_string.py