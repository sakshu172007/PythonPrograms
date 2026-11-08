def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for character in text.lower():
        if character in "aeiou":
            vowels = vowels + 1
        elif character.isalpha():
            consonants = consonants + 1

    return vowels, consonants


text = input("Enter a string: ")

vowels, consonants = count_vowels_consonants(text)

print("Vowels:", vowels)
print("Consonants:", consonants)


# python Code/11_vowels_consonants.py