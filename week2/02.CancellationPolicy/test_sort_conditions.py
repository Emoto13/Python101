import unittest
from cancellation_policy import sort_conditions

class TestSortConditions(unittest.TestCase):
    def test_if_sort_conditions_works_correctly(self):
        conditions = [
        {'hours': 6, 'percent': 80},
        {'hours': 12, 'percent': 50},
        {'hours': 24, 'percent': 10},
        {'hours': 0, 'percent': 100}
        ]
        
        result = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'hours': 0, 'percent': 100}
        ]
        conditions = sort_conditions(conditions)

        self.assertEqual(conditions, result)


    def test_if_sort_conditions_works_correctly_for_one_element(self):
        conditions = [
        {'hours': 0, 'percent': 100}
        ]

        result = [
        {'hours': 0, 'percent': 100}
        ]

        conditions = sort_conditions(conditions)

        self.assertEqual(conditions, result)




if __name__ == '__main__':
    unittest.main()