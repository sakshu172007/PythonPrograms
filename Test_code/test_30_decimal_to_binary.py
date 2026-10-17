from code.decimal_to_binary import decimal_to_binary


def test_decimal_to_binary():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(5) == "101"
    assert decimal_to_binary(8) == "1000"
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(15) == "1111"