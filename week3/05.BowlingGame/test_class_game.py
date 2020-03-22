import unittest
from solution import Game


class TestGameClass(unittest.TestCase):
    def test_if_game_class_works_with_strikes_only(self):
        g = Game([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        res = g.result
        exp = 300
        self.assertEqual(res, exp)

    def test_if_game_class_works_with_spares_only(self):
        g = Game([9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9])
        res = g.result
        exp = 190
        self.assertEqual(res, exp)

    def test_if_game_class_works_with_zeros_only(self):
        g = Game([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        res = g.result
        exp = 0
        self.assertEqual(res, exp)

    def test_if_game_class_works_with_spares_and_strikes(self):
        g = Game([10, 9, 1, 10, 9, 1, 10, 9, 1, 10, 9, 1, 10, 9, 1, 10])
        res = g.result
        exp = 200
        self.assertEqual(res, exp)

    def test_if_game_class_works_without_strikes_and_spares(self):
        g = Game([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])
        res = g.result
        exp = 65
        self.assertEqual(res, exp)

    def test_if_game_class_doesnt_work_for_wrong_length_of_frames(self):
        res = None
        try:
            g = Game([5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])
        except Exception as e:
            res = str(e)
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()
