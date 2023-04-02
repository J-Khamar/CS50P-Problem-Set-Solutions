from working import convert
import pytest

def test_twelve():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_regex():
    with pytest.raises(ValueError):
        convert("9 AM - 12 PM")

def test_ranges():
    with pytest.raises(ValueError):
        convert("12:60 PM to 5 AM")
