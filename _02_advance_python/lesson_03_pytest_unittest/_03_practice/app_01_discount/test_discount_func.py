import unittest

from _02_advance_python.lesson_03_pytest_unittest._03_practice.app_01_discount.discount_func import calculate_discount
# from discount_func import calculate_discount


class TestCalculateDiscount(unittest.TestCase):
    def setUp(self):
        self.values = ['basic', 'silver', 'gold']

    def test_basic_discount(self):
        self.assertEqual(calculate_discount(self.values[0], 100), 95)

    def test_silver_discount(self):
        self.assertEqual(calculate_discount(self.values[1], 100), 90)

    def test_gold_discount(self):
        self.assertEqual(calculate_discount(self.values[2], 100), 85)

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            calculate_discount('platinum', 80)


# if __name__ == '__main__':
#     unittest.main()
