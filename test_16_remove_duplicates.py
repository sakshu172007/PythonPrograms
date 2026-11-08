def remove_duplicates(numbers):
    return list(set(numbers))


assert sorted(remove_duplicates([1, 2, 2, 3, 4, 4])) == [1, 2, 3, 4]
assert sorted(remove_duplicates([5, 5, 5, 5])) == [5]
assert sorted(remove_duplicates([1, 2, 3])) == [1, 2, 3]
assert sorted(remove_duplicates([10, 20, 10, 30, 20])) == [10, 20, 30]
assert sorted(remove_duplicates([7, 7, 8, 8, 9])) == [7, 8, 9]

print("All test cases passed.")


# python Test_Code/test_16_remove_duplicates.py