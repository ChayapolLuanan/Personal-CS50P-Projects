import pytest
from fuel import convert
from fuel import gauge

def test_convert_valid_inputs():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("0/1") == 0

def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_invalid_value():
    with pytest.raises(ValueError):
        convert("3/2")  # X > Y

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("3.5/4")

    with pytest.raises(ValueError):
        convert("3/")

    with pytest.raises(ValueError):
        convert("/4")

def test_gauge_edges():
    assert gauge("0") == "E"
    assert gauge("1") == "E"
    assert gauge("99") == "F"
    assert gauge("100") == "F"

def test_gauge_middle_values():
    assert gauge("50") == "50%"
    assert gauge("75") == "75%"
    assert gauge("33") == "33%"
