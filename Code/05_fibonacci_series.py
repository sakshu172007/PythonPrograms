def fibonacci_series(number):
    series = []

    a = 0
    b = 1

    for i in range(number):
        series.append(a)
        a, b = b, a + b

    return series


number = int(input("Enter the number of terms: "))

print("Fibonacci Series:", fibonacci_series(number))


# python Code/05_fibonacci_series.py