def word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency


assert word_frequency("hello hello world") == {"hello": 2, "world": 1}
assert word_frequency("python is easy") == {"python": 1, "is": 1, "easy": 1}
assert word_frequency("apple apple apple") == {"apple": 3}
assert word_frequency("Hello hello") == {"hello": 2}
assert word_frequency("one two one") == {"one": 2, "two": 1}

print("All test cases passed.")


# python Test_Code/test_20_word_frequency.py