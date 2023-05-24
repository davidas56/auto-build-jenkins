import unittest

class TestMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_subtract_numbers(self):
        result = subtract_numbers(10, 4)
        self.assertEqual(result, 6)

    def test_multiply_numbers(self):
        result = multiply_numbers(2, 6)
        self.assertEqual(result, 12)

    def test_divide_numbers(self):
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == '__main__':
    unittest.main()
