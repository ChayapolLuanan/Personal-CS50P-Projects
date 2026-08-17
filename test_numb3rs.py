from numb3rs import validate

def test_amount_of_numbers():
    assert validate("124.2.2") == False
    assert validate("123.0") == False
    assert validate("123") == False
    assert validate("123.1.2.3.4") == False
    assert validate("123.1.2.3") == True

def test_leading_zeros():
    assert validate("124.01.1.2") == False
    assert validate("124.1.1.2") == True

def test_number_range():
    assert validate("257.11.1.2") == False
    assert validate("125.1.2.3") == True

def test_int():
    assert validate("cat") == False
    assert validate("CS50P") == False
    assert validate("cat.fun.cute.dog") == False
    assert validate("123.1.2.3") == True

def test_overall():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True
