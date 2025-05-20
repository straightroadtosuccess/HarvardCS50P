import pytest
from fuel import convert
from fuel import gauge


def test_convert_valid():
    assert convert("0/4") == 0
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("fuel/gauge")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
