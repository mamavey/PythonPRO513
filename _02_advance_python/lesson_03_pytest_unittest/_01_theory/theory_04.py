add = lambda a, b: a + b

divide = lambda a, b: a / b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 5) == 2
