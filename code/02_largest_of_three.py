def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(largest(10, 5, 8))
print(largest(3,15,7))
print(largest(4, 9, 12))