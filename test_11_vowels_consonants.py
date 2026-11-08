def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for character in text.lower():
        if character in "aeiou":
            vowels = vowels + 1
        elif character.isalpha():
            consonants = consonants + 1

    return vowels, consonants


assert count_vowels_consonants("hello") == (2, 3)
assert count_vowels_consonants("Hello World") == (3, 7)
assert count_vowels_consonants("Python") == (1, 5)
assert count_vowels_consonants("AEIOU") == (5, 0)
assert count_vowels_consonants("123") == (0, 0)

print("All test cases passed.")


# python Test_Code/test_11_vowels_consonants.py