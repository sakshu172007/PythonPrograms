def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


assert check_number(10) == "Positive"
assert check_number(-5) == "Negative"
assert check_number(0) == "Zero"
assert check_number(25) == "Positive"
assert check_number(-20) == "Negative"

print("All test cases passed.")


# python Test_Code/test_03_pos_neg_zero.py