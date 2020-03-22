import unittest
from collect_fractions import expand_fractions

class TestExpandFraction(unittest.TestCase):
    def test_expand_fraction_when_all_fractions_are_different(self):
        fractions = [(1, 1), (1, 2), (1, 4)]
        common_denominator = 4
        res = expand_fractions(fractions, common_denominator)
        expected = [(4, 4), (2, 4), (1, 4)]
        self.assertEqual(res, expected)

    def test_expand_fraction_when_there_are_duplicate_fraction(self):
        fractions = [(1, 2), (1, 4), (1, 4)]
        common_denominator = 4
        res = expand_fractions(fractions, common_denominator)
        expected = [(2, 4), (1, 4), (1, 4)]
        self.assertEqual(res, expected)    
    


if __name__ == '__main__':
    unittest.main()
