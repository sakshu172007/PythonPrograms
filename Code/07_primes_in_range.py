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


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime Numbers:", primes_in_range(start, end))


# python Code/07_primes_in_range.py