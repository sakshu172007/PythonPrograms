def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


assert find_largest(10, 20, 30) == 30
assert find_largest(50, 20, 40) == 50
assert find_largest(15, 70, 35) == 70
assert find_largest(25, 25, 25) == 25
assert find_largest(-10, -5, -20) == -5

print("All test cases passed.")

# python Test_Code/test_02_largest_of_three.py