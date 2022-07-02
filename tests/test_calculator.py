import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calculator = Calculator()

    def test_sumar(self):
        self.assertEqual(self.calculator.sumar(3, 2), 5)

    def test_multiplicar(self):
        self.assertEqual(self.calculator.multiplicar(3, 4), 1)


if __name__ == "__main__":
    unittest.main()