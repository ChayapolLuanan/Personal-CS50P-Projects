import bank
from bank import value

def test_value_correct():
    assert value("Hello") == 0
    assert value("hey") == 20
    assert value("what's up?") == 100
