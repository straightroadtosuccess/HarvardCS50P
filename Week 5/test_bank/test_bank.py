from bank import value


def test_alphanum():
    assert value("ABC123") == 100
    assert value("2025Q1") == 100


def test_lower():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("how you doing") == 20
    assert value("how's it going") == 20
    assert value("welcome") == 100
    assert value("what's happening") == 100
    assert value("what's up") == 100


def test_upper():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("HEY") == 20
    assert value("HOW YOU DOING") == 20
    assert value("HOW'S IT GOING") == 20
    assert value("WELCOME") == 100
    assert value("WHAT'S HAPPENING") == 100
    assert value("WHAT'S UP") == 100
