from um import count

def test_valid():
    assert count("Um, hi!") == 1

def test_zero_ums():
    assert count("mum") == 0
    assert count("yummy") == 0
