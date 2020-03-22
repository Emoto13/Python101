import unittest
from cancellation_policy import find_percent_corresponding_to_the_hours_left


class TestGroupConditions(unittest.TestCase):
    def test_if_find_percent_corresponding_to_the_hours_left_works_correctly(self):
        conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'hours': 0, 'percent': 100}
        ]

        percent = find_percent_corresponding_to_the_hours_left(6, conditions)
        result_percent = 80


        self.assertEqual(result_percent, percent)   


if __name__ == '__main__':
    unittest.main()