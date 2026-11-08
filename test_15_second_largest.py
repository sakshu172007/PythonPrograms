def second_largest(numbers):
    numbers = sorted(set(numbers))
    return numbers[-2]


assert second_largest([10, 20, 30, 40]) == 30
assert second_largest([5, 10, 15]) == 10
assert second_largest([100, 50, 75, 25]) == 75
assert second_largest([1, 2, 3, 4, 5]) == 4
assert second_largest([20, 10, 30, 40, 50]) == 40

print("All test cases passed.")


# python Test_Code/test_15_second_largest.py