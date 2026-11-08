def char_frequency(text):
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] = frequency[character] + 1
        else:
            frequency[character] = 1

    return frequency


assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert char_frequency("abc") == {"a": 1, "b": 1, "c": 1}
assert char_frequency("aabb") == {"a": 2, "b": 2}
assert char_frequency("aaa") == {"a": 3}
assert char_frequency("python") == {"p": 1, "y": 1, "t": 1, "h": 1, "o": 1, "n": 1}

print("All test cases passed.")


# python Test_Code/test_14_char_frequency.py