import unittest
from solution import Song


class TestSongClass(unittest.TestCase):
    def test_if_constructor_sets_values_correctly(self):
        song = Song(title="A", artist="B", album="C", length="1:00")
        expected = ["A", "B", "C", "1:00"]
        res = [song.title, song.artist, song.album, song.length]
        self.assertEqual(expected, res)

    def test_if_length_with_seconds_True_works_correctly(self):
        song = Song(title="A", artist="B", album="C", length="1:00")
        exp = 60
        res = song.get_length(seconds=True)
        self.assertEqual(exp, res)

    def test_if_length_with_minutes_True_works_correctly(self):
        song = Song(title="A", artist="B", album="C", length="1:00")
        exp = 1
        res = song.get_length(minutes=True)
        self.assertEqual(exp, res)

    def test_if_length_with_hours_True_works_correctly(self):
        song = Song(title="A", artist="B", album="C", length="1:00:00")
        exp = 1
        res = song.get_length(hours=True)
        self.assertEqual(exp, res)

    def test_if_length_without_arguments_works_correctly(self):
        song = Song(title="A", artist="B", album="C", length="1:00:00")
        exp = "1:00:00"
        res = song.get_length()
        self.assertEqual(exp, res)

    def test_if_str_dunder_works_correctly(self):
        song = Song(title="A", artist="B", album="C", length="1:00:00")
        exp = 'B - A from C - 1:00:00'
        self.assertEqual(exp, str(song))

    def test_if_repr_dunder_works_correctly(self):
        song = Song(title="A", artist="B", album="C", length="1:00:00")
        exp = 'B - A from C - 1:00:00'
        self.assertEqual(exp, repr(song))

    def test_if_eq_dunder_returns_False_for_different_objects(self):
        song1 = Song(title="A", artist="A", album="A", length="1:00:00")
        song2 = Song(title="B", artist="B", album="B", length="1:00:00")
        self.assertFalse(song1 == song2)

    def test_if_eq_dunder_returns_True_for_equal_objects(self):
        song1 = Song(title="A", artist="A", album="A", length="1:00:00")
        song2 = Song(title="A", artist="A", album="A", length="1:00:00")
        self.assertTrue(song1 == song2)


if __name__ == '__main__':
    unittest.main()
