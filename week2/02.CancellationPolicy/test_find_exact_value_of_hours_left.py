import unittest
from cancellation_policy import find_exact_value_of_hours_left


class TestGroupConditions(unittest.TestCase):
    def test_check_if_find_exact_value_of_hours_left_works_correctly_for_value_in_intervals(self):
        intervals = [(24, 12), (12, 6), (6, 0)]
        hours_left = 4
        interval_hours_left = find_exact_value_of_hours_left(hours_left, intervals)
        result = 0
        self.assertEqual(interval_hours_left, result)   

    def test_check_if_find_exact_value_of_hours_left_returns_None_if_value_not_in_intervals(self):
        intervals = [(24, 12), (12, 6), (6, 0)]
        hours_left = 24
        interval_hours_left = find_exact_value_of_hours_left(hours_left, intervals)
        result = 12
        self.assertEqual(interval_hours_left, result)   
    


if __name__ == '__main__':
    unittest.main()