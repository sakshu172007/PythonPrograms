def remove_duplicates(numbers):
    return list(set(numbers))


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("List without duplicates:", remove_duplicates(numbers))


# python Code/16_remove_duplicates.py