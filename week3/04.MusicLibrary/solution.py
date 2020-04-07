from validation import Validation
from utils import update_name
import random
import json


# make TimeUnit work for minutes and seconds over 60
class TimeUnit:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.__simplify_time_units()

    def get_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def get_minutes(self):
        return self.hours * 60 + self.minutes

    def get_hours(self):
        return self.hours

    @classmethod
    def create_time_unit(cls, length):
        occurrences = length.count(':')
        if occurrences == 1:
            minutes = int(length[:length.index(':')])
            seconds = int(length[length.index(':') + 1:])
            return TimeUnit(minutes=minutes, seconds=seconds)

        hours = int(length[:length.index(':')])
        minutes = int(length[length.index(':') + 1:length.rindex(':')])
        seconds = int(length[length.rindex(':') + 1:])
        return TimeUnit(hours=hours, minutes=minutes, seconds=seconds)

    def __simplify_time_units(self):
        if self.seconds >= 60:
            bonus_minutes = self.seconds // 60
            self.seconds %= 60
            self.minutes += bonus_minutes

        if self.minutes >= 60:
            bonus_hours = self.minutes // 60
            self.minutes %= 60
            self.hours += bonus_hours


class Song:
    def __init__(self, title="", artist="", album="", length=""):
        Validation.validate_that_arguments_are_not_empty_strings(title, artist, album, length)
        Validation.validate_length(length)

        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.time_unit = TimeUnit.create_time_unit(length)

    def get_length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.time_unit.get_seconds()

        if minutes:
            return self.time_unit.get_minutes()

        if hours:
            return self.time_unit.get_hours()

        return self.length

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_album(self):
        return self.album

    def __str__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __repr__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __eq__(self, other):
        if type(other) is Song and hash(self) == hash(other):
            return True
        return False

    def __hash__(self):
        return hash(str(self))


class PlayList:
    def __init__(self, name="PlayList", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.__shuffle = True

        self.songs = []
        self.dict_of_artists = {}
        self.__current_song_index = -1

    def add_song(self, song):
        if type(song) is not Song:
            raise Exception("Wrong argument type")

        if song in self.songs:
            raise Exception("Song is already in the playlist")

        artist = song.get_artist()
        self.songs.append(song)

        if artist not in self.dict_of_artists:
            self.dict_of_artists[artist] = 0
        self.dict_of_artists[artist] += 1

    def remove_song(self, song):
        if type(song) is not Song:
            raise Exception("Wrong argument type")

        if song not in self.songs:
            raise Exception("Song is not in the playlist")

        artist = song.get_artist()
        self.songs.remove(song)

        self.dict_of_artists[artist] -= 1

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        return len(self.songs)

    def artists(self):
        return self.dict_of_artists

    def next_song(self):
        if not self.songs:
            raise Exception("PlayList  is empty")

        if self.__shuffle:
            random.shuffle(self.songs)
            self.__shuffle = False

        if self.repeat:
            return self.__handle_when_repeat_is_True()
        else:
            return self.__handle_when_repeat_is_False()

    def __handle_when_repeat_is_True(self):
        while True:
            self.__current_song_index += 1
            if self.__current_song_index == self.total_length():
                self.__current_song_index = 0
            song_to_return = self.songs[self.__current_song_index]
            return song_to_return

    def __handle_when_repeat_is_False(self):
        self.__current_song_index += 1
        if self.__current_song_index != self.total_length():
            song_to_return = self.songs[self.__current_song_index]
            return song_to_return
        raise Exception("You have reached the end of the playlist")

    def save(self):
        file_name = update_name(self.name)
        json_repr = self.toJSON()
        with open(f'playlist-data/{file_name}.json', 'w+') as file:
            file.write(json_repr)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    @classmethod
    def load(cls, path):
        with open(f'playlist-data/{path}', 'r') as file:
            data = file.read()
            json_repr = json.loads(data)
            return cls.create_playlist_instance_with_correct_attributes(json_repr)

    @classmethod
    def create_playlist_instance_with_correct_attributes(cls, json_repr):
        playlist = PlayList(name=json_repr["name"], repeat=json_repr["repeat"], shuffle=json_repr["shuffle"])
        for song in json_repr["songs"]:
            s = Song(title=song['title'], artist=song['artist'], album=song['album'], length=song['length'])
            time_unit = song['time_unit']
            s.time_unit = TimeUnit(hours=time_unit['hours'], minutes=time_unit['minutes'], seconds=time_unit['seconds'])
            playlist.add_song(s)
        playlist.dict_of_artists = json_repr["dict_of_artists"]
        return playlist
