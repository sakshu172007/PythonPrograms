from code.largest_word import largest_word


def test_largest_word():
    assert largest_word("Python is amazing") == "amazing"
    assert largest_word("I love programming") == "programming"
    assert largest_word("Hello world") == "Hello"
    assert largest_word("AI is great") == "great"