def find_missing(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2

    return total - sum(numbers)


assert find_missing([1, 2, 3, 5]) == 4
assert find_missing([1, 2, 4, 5]) == 3
assert find_missing([1, 3, 4, 5]) == 2
assert find_missing([2, 3, 4, 5]) == 1
assert find_missing([1, 2, 3, 4, 6]) == 5

print("All test cases passed.")


# python Test_Code/test_18_missing_number.py