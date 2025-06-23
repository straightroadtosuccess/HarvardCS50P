from um import count
import pytest


def test_one_um():
    assert count("um") == 1

def test_multiple_ums():
    assert count("um, um, um, um, um, um, um, um, um, um, um") == 11

def test_no_ums():
    assert count("the word is missing") == 0

def test_um_inside_word():
    assert count("um, this shouldn't be dumb") == 1

def test_um_is_capitalized():
    assert count("UM!") == 1

