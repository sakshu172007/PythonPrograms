def common_elements(list1, list2):
    return list(set(list1) & set(list2))


assert sorted(common_elements([1, 2, 3, 4], [3, 4, 5, 6])) == [3, 4]
assert sorted(common_elements([1, 2, 3], [4, 5, 6])) == []
assert sorted(common_elements([10, 20, 30], [20, 30, 40])) == [20, 30]
assert sorted(common_elements([1, 2, 2, 3], [2, 3, 4])) == [2, 3]
assert sorted(common_elements([5, 6, 7], [5, 6, 7])) == [5, 6, 7]

print("All test cases passed.")


# python Test_Code/test_17_common_elements.py