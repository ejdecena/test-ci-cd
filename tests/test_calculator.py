from unittest import TestCase
from calculator.calculator import Calculator


class TestCalculator(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calculator = Calculator()

    def test_sumar(self):
        self.assertEqual(self.calculator.sumar(3, 2), 5)

    def test_multiplicar(self):
        self.assertEqual(self.calculator.multiplicar(3, 4), 12)
