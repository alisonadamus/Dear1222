import unittest

def multiply(a, b):
    return a * b

class TestMathFunctions(unittest.TestCase):

    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-1, 5), -5)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 10), 0)


#unittest.main()



class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль!")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("Створення калькулятора...")
        self.calc = Calculator()

    def tearDown(self):
        print("Завершення тесту...")

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


unittest.main()
