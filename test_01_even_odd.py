def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


assert check_even_odd(10) == "Even"
assert check_even_odd(7) == "Odd"
assert check_even_odd(0) == "Even"
assert check_even_odd(4) == "Even"
assert check_even_odd(9) == "Odd"

print("All test cases passed.")