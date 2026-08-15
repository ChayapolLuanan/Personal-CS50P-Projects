from plates import is_valid

#check for the order and position of the numbers in the plate
def test_number_placment():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50S") == False

def test_alphabetical():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("CS50CS") == False

def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

#check for the type of punctuation
def test_alphanumeric_char():
    assert is_valid("CS!!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False

#check for the number length of the plate number
def test_length():
    assert is_valid("blah") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False

def test_beginning_letters():
    assert is_valid("12") == False
    assert is_valid("A12AA6") == False
    assert is_valid("12AAA34B8") == False
