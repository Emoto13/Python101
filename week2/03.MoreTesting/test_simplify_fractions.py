import unittest
from simplify_fractions import simplify_fractions

class TestSimplifyFractions(unittest.TestCase):
    def test_if_simplify_fractions_works_for_two_equal_numbers(self):
        fraction = (2, 2)
        fraction = simplify_fractions(fraction)
        res = (1, 1)
        self.assertEqual(fraction, res)

    def test_if_simplify_fractions_works_for_two_numbers_without_a_common_denominator(self):
        fraction = (2, 3)
        fraction = simplify_fractions(fraction)
        res = (2, 3)
        self.assertEqual(fraction, res)
                
    
    def test_if_simplify_fractions_raises_exception_when_denominator_is_zero(self):
        fraction = (1, 0)
        res = None
        try:
            fraction = simplify_fractions(fraction)
        except Exception as exc:
            res = str(exc)    
        self.assertEqual(res, 'Denominator cannot be zero')

    def test_if_simplify_fractions_returns_tuple_of_two_zeros_when_nominator_is_zero(self):
        fraction = (0, 1)
        res = (0, 0)
        fraction = simplify_fractions(fraction)   
        
        self.assertEqual(fraction, res)    

    def test_if_simplify_fractions_raises_exception_when_input_is_not_a_tuple(self):
        fraction = [1, 1]
        res = None
        try:
            fraction = simplify_fractions(fraction)
        except Exception as exc:
            res = str(exc)    
        self.assertEqual(res, 'Function argument must be a tuple')

    def test_if_simplify_fractions_works_for_numbers_which_should_be_simplified_more_than_once(self):
        fraction = (8, 16)
        res = (1, 2)

        fraction = simplify_fractions(fraction)
        self.assertEqual(res, fraction)

    def test_if_simplify_fractions_works_for_negative_fraction(self):
        fraction = (-8, 16)
        res = (-1, 2)

        fraction = simplify_fractions(fraction)
        self.assertEqual(res, fraction)


            


if __name__ == '__main__':
    unittest.main()
