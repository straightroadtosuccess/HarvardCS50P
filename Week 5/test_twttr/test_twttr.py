from twttr import shorten


def test_function():
    assert shorten("Education") == "dctn"
    assert shorten("Audio") == "d"


def test_alphanum():
    assert shorten("ABC123") == "BC123"
    assert shorten("2025Q1") == "2025Q1"


def test_lower():
    assert shorten("Facebook") == "Fcbk"
    assert shorten("Instagram") == "nstgrm"


def test_upper():
    assert shorten("GOOGLE") == "GGL"
    assert shorten("YOUTUBE") == "YTB"


def test_punctuation():
    assert shorten("Hello!") == str("Hll!")
    assert shorten("readme.md") == str("rdm.md")


def test_type():
    assert shorten("Cat") == str("Ct")
    assert shorten("ERROR") == str("RRR")
