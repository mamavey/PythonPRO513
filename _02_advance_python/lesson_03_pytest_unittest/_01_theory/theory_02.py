import unittest


class TestExample(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.main()

"""
assertEqual(a, b) — проверяет, равны ли значения a и b.
assertNotEqual(a, b) — проверяет, что значения a и b не равны.
assertTrue(x) — проверяет, что значение x истинно.
assertFalse(x) — проверяет, что значение x ложно.
assertRaises(Exception, func, *args, **kwargs) — проверяет, что вызов функции func вызывает исключение Exception.
"""