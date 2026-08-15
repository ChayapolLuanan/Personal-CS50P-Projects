from twttr import shorten

def test_shorten_all_vowels():
    assert shorten("aeiou") == ""

def test_shorten_caps_check():
    assert shorten("AEIOU") == ""

def test_shorten_word():
    assert shorten("twitter") == "twttr"

def test_shorten_punctuation():
    assert shorten("twitter.py") == "twttr.py"
