import pytest
from project import text_to_binary
from project import binary_to_text
from project import process_csv

def test_text_to_binary():
    assert text_to_binary("CS50") == "01000011 01010011 00110101 00110000"
    assert text_to_binary("Hello my name is Julien") == "01001000 01100101 01101100 01101100 01101111 00100000 01101101 01111001 00100000 01101110 01100001 01101101 01100101 00100000 01101001 01110011 00100000 01001010 01110101 01101100 01101001 01100101 01101110"

def test_binary_to_text():
    assert binary_to_text("01001000 01100101 01101100 01101100 01101111") == "Hello"
    assert binary_to_text("01110000 01110010 01101111 01101010 01100101 01100011 01110100") == "project"
    assert binary_to_text("01110100 01100101 01110011 01110100") == "test"

def test_process_csv():
    with pytest.raises(SystemExit):
        process_csv("non_existent_file.csv", "output.csv", "encode")
    with pytest.raises(SystemExit):
        process_csv("non_existent_file.csv", "output.csv", "decode")
    with pytest.raises(SystemExit):
        process_csv("non_existent_file.csv", "output.csv", "non_existent_mode")

