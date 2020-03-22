import unittest
from sort_fractions import sort_fractions

class TrestSortFractions(unittest.TestCase):
    def test_if_sort_fractions_works_when_all_fractions_are_different(self):
        fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        res = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]

        fractions = sort_fractions(fractions)
        self.assertEqual(fractions, res)

    def test_if_sort_fractions_works_when_there_are_duplicate_elements(self):
        fractions = [(5, 6), (22, 78), (5, 6), (22, 7), (9, 6), (7, 8), (9, 6), (15, 32)]
        res = [(22, 78), (15, 32), (5, 6), (5, 6), (7, 8), (9, 6), (9, 6), (22, 7)]

        fractions = sort_fractions(fractions)
        self.assertEqual(fractions, res)

    def test_if_sort_fractions_works_when_ascending_is_false(self):
        fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        res = [(22, 7), (9, 6), (7, 8), (5, 6), (15, 32), (22, 78)]

        fractions = sort_fractions(fractions, ascending = False)
        self.assertEqual(fractions, res)

    def test_if_sort_fractions_works_when_ascending_is_true(self):
        fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        res = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
        fractions = sort_fractions(fractions, ascending = True)
        self.assertEqual(fractions, res)

    def test_if_sort_fractions_raises_exception_when_input_is_not_a_list(self):
        fractions = 'I am a list'

        res = None
        try:
            sort_fractions(fractions)
        except ValueError as exc:
            res = str(exc)
        self.assertEqual(res, 'Input must be a list of tuples')  

    def test_if_sort_fractions_raises_exception_when_input_is_an_empty_list(self):
        fractions = []

        res = None
        try:
            sort_fractions(fractions)
        except ValueError as exc:
            res = str(exc)
        self.assertEqual(res, 'Input cannot be an empty list') 


    def test_if_sort_fractions_raises_exception_when_input_is_heterogeneous_list(self):
        fractions = [(1,2), (3, 4), 23, {'a': 1}]

        res = None
        try:
            sort_fractions(fractions)
        except ValueError as exc:
            res = str(exc)
        self.assertEqual(res, 'Input must only consist of fractions(tuples)')

    def test_if_sort_fractions_raises_exception_when_fractions_contain_denominator_with_zero(self):
        fractions = [(1,2), (3, 4), (0, 4), (4, 0)]

        res = None
        try:
            sort_fractions(fractions)
        except ValueError as exc:
            res = str(exc)
        self.assertEqual(res, 'Fraction with 0 as denominator')


if __name__ == '__main__':
    unittest.main()