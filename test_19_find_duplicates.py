def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates


assert find_duplicates([1, 2, 2, 3, 4, 4]) == [2, 4]
assert find_duplicates([1, 2, 3, 4]) == []
assert find_duplicates([5, 5, 5]) == [5]
assert find_duplicates([1, 1, 2, 2, 3]) == [1, 2]
assert find_duplicates([10, 20, 10, 30, 20]) == [10, 20]

print("All test cases passed.")


# python Test_Code/test_19_find_duplicates.py