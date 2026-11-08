def word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency


text = input("Enter a sentence: ")

print("Word Frequency:", word_frequency(text))


# python Code/20_word_frequency.py