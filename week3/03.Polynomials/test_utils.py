import unittest
from utils import validate_polynomial, simplify_polynomial


class TestUtilFunctions(unittest.TestCase):
    def test_if_validate_polynomial_raises_exception_when_polynomial_is_not_string(self):
        polynomial = 5
        res = None
        try:
            validate_polynomial(polynomial)
        except TypeError as e:
            res = str(e)
        self.assertEqual(res, "Polynomial must be a string")

    def test_if_validate_polynomial_raises_exception_when_polynomial_contains_minuses(self):
        polynomial = 'x^2 - 2x + 1'
        res = None
        try:
            validate_polynomial(polynomial)
        except ValueError as e:
            res = str(e)
        self.assertEqual(res, "Polynomial shouldn't contain minuses")

    def test_if_simplify_polynomial_works_correctly_for_string_with_spaces(self):
        polynomial = 'x^2 + 2x + 1'
        simple_polynomial = simplify_polynomial(polynomial)
        res = 'x^2+2x+1'
        self.assertEqual(res, simple_polynomial)

    def test_if_simplify_polynomial_works_correctly_for_string_without_spaces(self):
        polynomial = 'x^2+2x+1'
        simple_polynomial = simplify_polynomial(polynomial)
        res = 'x^2+2x+1'
        self.assertEqual(res, simple_polynomial)

    def test_if_simplify_polynomial_works_correctly_for_string_with_asterisk(self):
        polynomial = '2*x^2+2*x+1'
        simple_polynomial = simplify_polynomial(polynomial)
        res = '2x^2+2x+1'
        self.assertEqual(res, simple_polynomial)


if __name__ == '__main__':
    unittest.main()
