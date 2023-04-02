from plates import is_valid

def test_start():
    assert is_valid("A150") == False

def test_length():
    assert is_valid("AAA1283") == False

def test_zero_placement():
    assert is_valid("AA012") == False

def test_middle_num():
    assert is_valid("AA2AA") == False

def test_characters():
    assert is_valid("AA,") == False