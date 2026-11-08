def fibonacci_series(number):
    series = []

    a = 0
    b = 1

    for i in range(number):
        series.append(a)
        a, b = b, a + b

    return series


assert fibonacci_series(1) == [0]
assert fibonacci_series(2) == [0, 1]
assert fibonacci_series(5) == [0, 1, 1, 2, 3]
assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
assert fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print("All test cases passed.")


# python Test_Code/test_05_fibonacci_series.py