import unittest


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('На ноль делить нельзя!')
    return a / b

class TestDivideFunction(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, divide, 10, 0)
