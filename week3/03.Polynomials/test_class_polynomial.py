import unittest
from solution import Polynomial, Term


class TestPolynomialClass(unittest.TestCase):
    def test_if_constructor_sets_terms_correctly(self):
        polynomial = '3x^2+2x+1'
        p = Polynomial(polynomial)
        res = ['6*x', '2']
        self.assertEqual(res, p.get_terms())

    def test_if_find_derivative_works_correctly_for_polynomial_with_x(self):
        polynomial = '3x^2+2x+1'
        p = Polynomial(polynomial)
        res = '6*x+2'
        self.assertEqual(res, p.find_derivative())

    def test_if_find_derivative_works_correctly_for_polynomial_without_x(self):
        polynomial = '5'
        p = Polynomial(polynomial)
        res = '0'
        self.assertEqual(res, p.find_derivative())


if __name__ == '__main__':
    unittest.main()
