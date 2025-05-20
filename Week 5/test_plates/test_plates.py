from plates import is_valid


def test_is_valid_plates():
    assert is_valid("cs50") == True


def test_non_alphanumeric():
    assert is_valid("AB$12") == False


def test_invalid_start_letters():
    assert is_valid("12345") == False


def test_invalid_zero():
    assert is_valid("AB012") == False


def test_invalid_length():
    assert is_valid("ABCDEFG") == False


def test_invalid_number_placement():
    assert is_valid("AB12C") == False
