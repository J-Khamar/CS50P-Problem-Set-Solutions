from numb3rs import validate

def test_format():
    assert validate("cat") == False

def test_datatype():
    assert validate("cat.1.2.3") == False

def test_range():
    assert validate("1.2.3.270") == False