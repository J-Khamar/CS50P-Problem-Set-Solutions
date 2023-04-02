from twttr import shorten

def test_word():
    assert shorten("twittr") == "twttr"

def test_sentence():
    assert shorten("hello world") == "hll wrld"

def test_punctuation():
    assert shorten("hello, world") == "hll, wrld"

def test_casing():
    assert shorten("HellO") == "Hll"

def test_numbers():
    assert shorten("123") == "123"