def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates


numbers = list(map(int, input("Enter numbers: ").split()))

print("Duplicate Elements:", find_duplicates(numbers))


# python Code/19_find_duplicates.py