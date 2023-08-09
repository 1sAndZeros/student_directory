from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, 'Test Album', 2000, 4)
    assert album.id == 1
    assert album.title == 'Test Album'
    assert album.release_year == 2000
    assert album.artist_id == 4

"""
We can format albums to strings nicely
"""
def test_album_formatting():
    album = Album(1, 'Test Album', 2000, 4)
    assert str(album) == "Album(1, Test Album, 2000, 4)"

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, 'Test Album', 2000, 4)
    album2 = Album(1, 'Test Album', 2000, 4)
    assert album1 == album2
