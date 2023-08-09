from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call albumRepository#all
We get a list of album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]

    assert len(albums) == 12

    assert albums[0].id == 1
    assert albums[0].title == 'Doolittle'
    assert albums[0].release_year == 1989
    assert albums[0].artist_id == 1

    assert albums[1].id == 2
    assert albums[1].title == 'Surfer Rosa'
    assert albums[1].release_year == 1988
    assert albums[1].artist_id == 1

    assert albums[2].id == 3
    assert albums[2].title == 'Waterloo'
    assert albums[2].release_year == 1974
    assert albums[2].artist_id == 2

def test_find_album_by_id(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository
    album = repository.find(1)
    assert album.id == 1

'''
when we call AlbumRepository #create
we get a new record in the database
'''

def test_create_album(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    repo.create(Album(None, 'Midnight', 2022, 3))
    result = repo.all()
    assert result == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
        Album(13, "Midnight", 2022, 3)
    ]

    """
    Test delete record by id
    """

def test_delete_record_by_id(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    repo.delete(8)
    result = repo.all()
    assert result == [
            Album(1, "Doolittle", 1989, 1),
            Album(2, "Surfer Rosa", 1988, 1),
            Album(3, "Waterloo", 1974, 2),
            Album(4, "Super Trouper", 1980, 2),
            Album(5, "Bossanova", 1990, 1),
            Album(6, "Lover", 2019, 3),
            Album(7, "Folklore", 2020, 3),
            Album(9, "Baltimore", 1978, 4),
            Album(10, "Here Comes the Sun", 1971, 4),
            Album(11, "Fodder on My Wings", 1982, 4),
            Album(12, "Ring Ring", 1973, 2)
    ]