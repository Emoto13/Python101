import unittest
from solution import Term


class TestTermClass(unittest.TestCase):
    def test_if_term_constructor_works_for_term_without_coefficient(self):
        power = '2'
        term = Term(power=power)
        res = 1
        self.assertEqual(res, term.get_power())

    def test_if_term_constructor_works_for_term_without_power(self):
        coefficient = '2'
        term = Term(coefficient=coefficient)
        res = 2
        self.assertEqual(res, term.get_coefficient())

    def test_if_term_constructor_works_for_term_without_coefficient_and_power(self):
        power = '2'
        coefficient = '2'
        term = Term(coefficient=coefficient, power=power)
        res_coefficient = 4
        res_power = 1
        self.assertEqual(res_coefficient, term.get_coefficient())
        self.assertEqual(res_power, term.get_power())

    def test_if___str___works_for_term_without_coefficient(self):
        term = Term(power='2')
        res = str(term)
        self.assertEqual(res, '2*x')

    def test_if___str___constructor_works_for_term_without_power(self):
        term = Term(coefficient='2')
        res = str(term)
        self.assertEqual(res, '2')

    def test_if___str___works_for_term_without_coefficient_and_power(self):
        term = Term(coefficient='2', power='3')
        res = str(term)
        self.assertEqual(res, '6*x^2')


if __name__ == '__main__':
    unittest.main()
