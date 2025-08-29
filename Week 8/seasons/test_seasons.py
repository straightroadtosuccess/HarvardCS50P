import pytest
from datetime import date, timedelta
from seasons import Birthday


# Test invalid dates
def test_invalid_date_format():
    with pytest.raises(SystemExit):
        Birthday("invalid-example-date")


# Test 1 day in minutes, outcome should be 1440 minutes
def test_age_one_day():
    one_day_ago = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    assert Birthday(one_day_ago).minutes_old() == 1440


# Test minutes converted to words
def test_words_for_minutes_format():
    words = Birthday((date.today() - timedelta(days=1)).strftime("%Y-%m-%d")).words_for_minutes()
    assert isinstance(words, str) and words[0].isupper() and " and " not in words
