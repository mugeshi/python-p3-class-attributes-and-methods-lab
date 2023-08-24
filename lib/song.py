class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.__class__.add_to_genres()
        self.__class__.add_to_artists()
        self.__class__.add_to_genre_count()
        self.__class__.add_to_artist_count()

        self.__class__.count += 1

    @classmethod
    def add_to_genres(cls):
        if cls.genre not in cls.genres:
            cls.genres.append(cls.genre)

    @classmethod
    def add_to_artists(cls):
        if cls.artist not in cls.artists:
            cls.artists.append(cls.artist)

    @classmethod
    def add_to_genre_count(cls):
        if cls.genre in cls.genre_count:
            cls.genre_count[cls.genre] += 1
        else:
            cls.genre_count[cls.genre] = 1

    @classmethod
    def add_to_artist_count(cls):
        if cls.artist in cls.artist_count:
            cls.artist_count[cls.artist] += 1
        else:
            cls.artist_count[cls.artist] = 1
