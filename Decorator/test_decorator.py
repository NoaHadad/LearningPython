from decorator import FunctionCounterDecorator


@FunctionCounterDecorator
def F(x: int, y: int) -> int:
    return x + y


def test_counter():
    f = F
    assert f.counter == 0
    f(0, 1)
    assert f.counter == 1
    f(0, 6)
    assert f.counter == 2


def test_call():
    f = F
    assert f(5, 1) == 6
    assert f(9, 2) == 11