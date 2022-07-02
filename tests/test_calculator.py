import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sumar(self):
        self.assertEqual(self.calculator.sumar(3, 2), 5)

    def test_multiplicar(self):
        self.assertEqual(self.calculator.multiplicar(3, 4), 12)
