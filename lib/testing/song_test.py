# song_test.py
from lib.song import Song

class TestSong:
    def test_saves_name_artist_genre(self):
        ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
        assert ninety_nine_problems.name == "99 Problems"
        assert ninety_nine_problems.artist == "Jay-Z"
        assert ninety_nine_problems.genre == "Rap"

    def test_has_song_count(self):
        assert Song.count == 1  # Update the expected count accordingly
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.count == 2  # Update the expected count accordingly

    def test_has_genres(self):
        assert "Pop" in Song.genres

    def test_has_artists(self):
        assert "Hall and Oates" in Song.artists
        
    def test_has_genre_count(self):
        assert Song.genre_count["Pop"] == 2  # Update the expected count accordingly

    def test_has_artist_count(self):
        assert Song.artist_count["Hall and Oates"] == 2  # Update the expected count accordingly
