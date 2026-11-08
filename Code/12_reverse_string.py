def reverse_string(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return reversed_text


text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))


# python Code/12_reverse_string.py