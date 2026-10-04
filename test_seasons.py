from seasons import find_minutes

def test_valid():
    assert find_minutes("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
