import unittest
from cancellation_policy import ensure_conditions


class TestEnsureConditions(unittest.TestCase):
    def test_if_ensure_conditions_method_works(self):
        conditions = [
            {'hours': 10, 'percent': 10000},
            {'percent': 10}
        ]

        ensure_conditions(conditions)
        result = [
            {'hours': 10, 'percent': 10000},
            {'hours': 0, 'percent': 10}
        ]

        self.assertEqual(conditions, result)


if __name__ == '__main__':
    unittest.main()
