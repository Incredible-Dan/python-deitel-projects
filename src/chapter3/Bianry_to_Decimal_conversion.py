import unittest
from .binary_to_decimal_conversion import binary_to_decimal


class TestBinaryToDecimal(unittest.TestCase):

    def test_binary_to_decimal_0(self):
        dec = binary_to_decimal(0)
        self.assertEquals(dec, 0)

    def test_binary_to_decimal_1(self):
        dec = binary_to_decimal(1)
        self.assertEquals(dec, 1)

    def test_binary_to_decimal_2(self):
        dec = binary_to_decimal(10)
        self.assertEquals(dec, 2)

    def test_binary_to_decimal_3(self):
        with self.assertRaises(TypeError):
            dec = binary_to_decimal("Hello")


if __name__ == '__main__':
    unittest.main()
