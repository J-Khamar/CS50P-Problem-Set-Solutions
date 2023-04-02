from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("cat/4")
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"