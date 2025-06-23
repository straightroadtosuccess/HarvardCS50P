from working import convert
import pytest


def test_times_that_are_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_times_that_are_not_valid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_edge_cases():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12 AM to 1 AM") == "00:00 to 01:00"
    assert convert("1 PM to 11 PM") == "13:00 to 23:00"
