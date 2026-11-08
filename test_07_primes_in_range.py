def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def primes_in_range(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert primes_in_range(10, 20) == [11, 13, 17, 19]
assert primes_in_range(2, 5) == [2, 3, 5]
assert primes_in_range(20, 25) == [23]

print("All test cases passed.")


# python Test_Code/test_07_primes_in_range.py