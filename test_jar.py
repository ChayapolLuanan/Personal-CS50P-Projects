from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

    my_jar = Jar(5)
    assert my_jar.capacity == 5

    with pytest.raises(ValueError):
        negative_capacity = Jar(-1)
        assert negative_capacity

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(12)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(12)
    jar.deposit(6)

    jar.withdraw(2)
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.withdraw(5)
