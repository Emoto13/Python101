import unittest
from cancellation_policy import check_if_hours_left_are_bigger_than_the_intervals


class TestGroupConditions(unittest.TestCase):
    def test_if_hours_left_are_bigger_than_the_intervals_method_works_for_bigger_interval(self):
        intervals = [(24, 12), (12, 6), (6, 0)]
        hours_left = 25
        interval_hours_left = check_if_hours_left_are_bigger_than_the_intervals(hours_left, intervals)    
        result = 24

        self.assertEqual(interval_hours_left, result)   

    def test_if_hours_left_are_bigger_than_the_intervals_method_works_for_smaller_interval(self):
        intervals = [(24, 12), (12, 6), (6, 0)]
        hours_left = 23
        interval_hours_left = check_if_hours_left_are_bigger_than_the_intervals(hours_left, intervals)    
        result = 23

        self.assertEqual(interval_hours_left, result)  


if __name__ == '__main__':
    unittest.main()