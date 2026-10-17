def largest_word(sentence):
    words = sentence.split()
    largest = ""

    for word in words:
        if len(word) > len(largest):
            largest = word

    return largest