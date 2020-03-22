import unittest
from cancellation_policy import group_conditions


class TestGroupConditions(unittest.TestCase):
    def test_if_group_conditions_method_works_correctly_with_even_number_of_elements(self):
        conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'hours': 0, 'percent': 100}
        ]

        result = [(24, 12), (12, 6), (6, 0)]
        conditions = group_conditions(conditions)    

        self.assertEqual(conditions, result)   

    def test_if_group_conditions_method_if_there_is_only_one_condition(self):
        conditions = [
        {'hours': 0, 'percent': 100}
        ]

        result = [(24 ,0)]
        conditions = group_conditions(conditions)    


        self.assertEqual(conditions, result)  

    def test_if_group_conditions_method_works_correctly_with_odd_number_of_elements(self):
        conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 18, 'percent': 20},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'hours': 0, 'percent': 100}
        ]

        result = [(24, 18), (18, 12), (12, 6), (6, 0)]
        conditions = group_conditions(conditions)    

        self.assertEqual(conditions, result)   
    


if __name__ == '__main__':
    unittest.main()