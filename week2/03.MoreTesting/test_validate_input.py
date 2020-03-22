import unittest
from collect_fractions import ensure_input_is_a_list, ensure_input_is_not_an_empty_list, ensure_input_is_a_homogeneous_list, ensure_input_doesnt_contain_denominator_with_zero

class TestValidateInput(unittest.TestCase):
    def test_ensure_input_is_a_list_must_raise_exception_when_input_is_not_a_list(self):
        fractions = 'I am a list'

        res = None
        try:
            ensure_input_is_a_list(fractions)
        except ValueError as exc:
            res = str(exc)
        self.assertEqual(res, 'Input must be a list of tuples')  

    def test_ensure_input_is_not_an_empty_list_must_raise_exception_when_input_is_an_empty_list(self):
        fractions = []

        res = None
        try:
            ensure_input_is_not_an_empty_list(fractions)
        except ValueError as exc:
            res = str(exc)
        self.assertEqual(res, 'Input cannot be an empty list') 


    def test_ensure_input_is_a_homogeneous_list_must_raise_exception_when_input_is_heterogeneous_list(self):
        fractions = [(1,2), (3, 4), 23, {'a': 1}]

        res = None
        try:
            ensure_input_is_a_homogeneous_list(fractions)
        except ValueError as exc:
            res = str(exc)
        self.assertEqual(res, 'Input must only consist of fractions(tuples)')

    def test_ensure_input_doesnt_contain_denominator_with_zero(self):
        fractions = [(1,2), (3, 4), (0, 4), (4, 0)]

        res = None
        try:
            ensure_input_doesnt_contain_denominator_with_zero(fractions)
        except ValueError as exc:
            res = str(exc)
        self.assertEqual(res, 'Fraction with 0 as denominator')

if __name__ == '__main__':
    unittest.main()
