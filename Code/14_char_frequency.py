def char_frequency(text):
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] = frequency[character] + 1
        else:
            frequency[character] = 1

    return frequency


text = input("Enter a string: ")

print("Character Frequency:", char_frequency(text))


# python Code/14_char_frequency.py