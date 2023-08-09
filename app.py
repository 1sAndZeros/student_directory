from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
    # "Runs" the terminal application.

    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
        choice = 0
        while not choice in ['1', '2']:
            choice = input('''
            Welcome to the music library manager!
            
            What would you like to do?
                1 - List all albums
                2 - List all artists
            
            Enter your choice: 
            ''')
            if choice == '1':
                artist_repository = ArtistRepository(self._connection)
                artists = artist_repository.all()

                for artist in artists:
                    print(f"{artist.id} - {artist.name} - {artist.genre}")

            elif choice == '2':
                album_repository = AlbumRepository(self._connection)
                albums = album_repository.all()

                for album in albums:
                    print(f"{album.id} - {album.title} - {album.release_year}")
            
            else:
                print('Choice is incorrect. Please choose 1 or 2!')

if __name__ == '__main__':
    app = Application()
    app.run()