import pytest
from iterator import SimpleListIterator


@pytest.fixture
def iterator():
    simple_iterator = SimpleListIterator([1, 2, 3, 4, 5])
    yield simple_iterator
    del simple_iterator


@pytest.fixture
def dafault_iterator():
    simple_iterator = SimpleListIterator()
    yield simple_iterator
    del simple_iterator


def test_iterator_init(iterator, dafault_iterator):
    assert str(iterator) == "SimpleListIterator(_arr=[1, 2, 3, 4, 5])"
    assert str(dafault_iterator) == "SimpleListIterator(_arr=[])"


def test_iterate(iterator, dafault_iterator):
    current = 1
    my_iterator = iter(iterator)
    for num in my_iterator:
        assert current == num
        current += 1
    with pytest.raises(StopIteration) as e:
        next(dafault_iterator)