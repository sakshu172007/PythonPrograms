def find_missing(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2

    return total - sum(numbers)


numbers = list(map(int, input("Enter numbers: ").split()))

print("Missing Number:", find_missing(numbers))


# python Code/18_missing_number.py