def sum_of_digits(number):
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    return total


number = int(input("Enter a number: "))

print("Sum of digits:", sum_of_digits(number))


# python Code/10_sum_of_digits.py