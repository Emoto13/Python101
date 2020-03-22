import unittest
import os
from solution import PlayList, Song


class TestPlayListClass(unittest.TestCase):
    test_song1 = Song(title="Soldi", artist="Mahmood", album="Unknown", length="3:24")
    test_song2 = Song(title="Mesecina", artist="Goran Bregovic", album="Unknown", length="3:50")

    def test_if_constructor_sets_values_correctly(self):
        playList = PlayList(name="List", repeat=True, shuffle=True)
        exp = ["List", True, True]
        res = [playList.name, playList.repeat, playList.shuffle]
        self.assertEqual(res, exp)

    def test_if_add_song_raises_Exception_when_the_song_already_exists(self):
        playList = PlayList()
        playList.add_song(self.test_song1)
        test_song1_copy = Song(title="Soldi", artist="Mahmood", album="Unknown", length="3:24")

        exp = "Song is already in the playlist"
        res = None
        try:
            playList.add_song(test_song1_copy)
        except Exception as e:
            res = str(e)
        self.assertEqual(res, exp)

    def test_if_add_song_raises_Exception_when_the_argument_is_not_of_type_Song(self):
        playList = PlayList()
        exp = "Wrong argument type"
        res = None
        try:
            playList.add_song('a')
        except Exception as e:
            res = str(e)
        self.assertEqual(res, exp)

    def test_if_add_song_works_correctly_for_valid_song(self):
        playList = PlayList()
        playList.add_song(self.test_song1)
        exp = 1
        res = len(playList.songs)
        self.assertEqual(res, exp)

    def test_if_remove_song_raises_Exception_when_song_doesnt_exist(self):
        playList = PlayList()
        exp = "Song is not in the playlist"
        res = None
        try:
            playList.remove_song(self.test_song1)
        except Exception as e:
            res = str(e)
        self.assertEqual(res, exp)

    def test_if_remove_song_raises_Exception_when_the_argument_is_not_of_type_Song(self):
        playList = PlayList()
        exp = "Wrong argument type"
        res = None
        try:
            playList.remove_song("a")
        except Exception as e:
            res = str(e)
        self.assertEqual(res, exp)

    def test_if_remove_song_works_correctly_for_valid_song(self):
        playlist = PlayList()
        playlist.add_song(self.test_song1)
        playlist.remove_song(self.test_song1)

        exp = 0
        res = len(playlist.songs)
        self.assertEqual(res, exp)

    def test_if_total_length_works_correctly(self):
        playlist = PlayList()
        exp = 0
        res = playlist.total_length()
        self.assertEqual(res, exp)

    def test_if_add_songs_works_correctly(self):
        playlist = PlayList()
        songs = [self.test_song1, self.test_song2]
        playlist.add_songs(songs)
        exp = 2
        res = playlist.total_length()
        self.assertEqual(res, exp)

    def test_if_artists_works_correctly(self):
        playlist = PlayList()
        playlist.add_song(self.test_song1)
        playlist.add_song(self.test_song2)
        exp = {'Goran Bregovic': 1, 'Mahmood': 1}
        res = playlist.artists()
        self.assertEqual(res, exp)

    def test_if_next_song_works_correctly_for_repeat_True(self):
        playlist = PlayList(repeat=True)
        playlist.add_song(self.test_song1)
        playlist.next_song()
        res = playlist.next_song()
        exp = self.test_song1
        self.assertEqual(res, exp)

    def test_if_next_song_raises_Exception_for_empty_playlist(self):
        playlist = PlayList()
        res = None
        exp = "PlayList  is empty"
        try:
            playlist.next_song()
        except Exception as e:
            res = str(e)
        self.assertEqual(res, exp)

    def test_if_next_song_raises_Exception_when_reaches_the_end_of_the_list_and_range_False(self):
        playlist = PlayList()
        playlist.add_song(self.test_song1)

        res = None
        exp = "You have reached the end of the playlist"
        playlist.next_song()
        try:
            playlist.next_song()
        except Exception as e:
            res = str(e)
        self.assertEqual(res, exp)

    def test_if_save_and_load_works_correctly(self):
        playlist = PlayList(name="For Code")
        playlist.add_song(self.test_song1)
        playlist.add_song(self.test_song2)
        playlist.save()
        playlist2 = PlayList.load('For-Code.json')

        res = playlist.songs == playlist2.songs \
              and playlist.name == playlist2.name \
              and playlist.artists() == playlist2.artists()

        self.assertTrue(res)
        os.remove('playlist-data/For-Code.json')


if __name__ == '__main__':
    unittest.main()
