from numb3rs import validate


def test_amountofdots():
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4") == True


def test_invalidcharacters():
    assert validate("cat") == False
    assert validate("dog") == False


def test_numberstoohigh():
    assert validate("275.0.0.0") == False
    assert validate("0.300.0.0") == False
    assert validate("286.255.255.255") == False
    assert validate("255.255.255.255") == True
