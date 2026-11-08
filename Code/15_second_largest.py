def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number

    return second


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Second Largest Number:", second_largest(numbers))


# python Code/15_second_largest.py