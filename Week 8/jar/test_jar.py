from jar import Jar


def test_init():
    assert Jar(5).capacity == 5
    assert Jar().capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(3)
    jar.deposit(2)
    assert jar.size == 2


def test_withdraw():
    jar = Jar(3)
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2
