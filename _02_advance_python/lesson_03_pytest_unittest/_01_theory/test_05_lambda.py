import pytest


@pytest.fixture
def add_data():
    return 4, 2


add = lambda a, b: a + b


def test_add(add_data):
    a = add_data[0]
    b = add_data[1]
    assert add(a, b) == 6
