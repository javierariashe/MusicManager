from linearSearch import *
from artist import *
from playlist import *


def tu_biblioteca(user, artists, new_path):
    while True:
        print("\nBiblioteca")
        print("1. Buscar artista")
        print("2. Playlists")
        print("3. Agregar canciones")
        print("4. Regresar")
        try:
            op = int(input())
            match op:
                case 1:
                    show_artist(user, artists)
                case 2:
                    playlists(user)
                case 3:
                    add_songs(user, new_path)
                    artists = read_artist_csv(user)
            if op == 4:
                break
        except ValueError:
            print("Por favor, introduce un número válido.")


def show_artist(user, artists):
    artist_name = str(input("Ingrese el nombre del artista: "))
    artista = artists.search(artists.root, artist_name)
    if artista is not None:
        op = 0
        while op != 2:
            print("\n1. Ver canciones")
            print("2. Regresar")
            try:
                op = int(input())
                match op:
                    case 1:
                        song = show_songs(artista)
                        if song is not None:
                            add_to_playlist(user, song)
            except ValueError:
                print("Por favor, introduce un número válido.")
    else:
        print("El artista ingresado no esta agregado en tu biblioteca")


def show_songs(artista):
    print("Canciones:")
    i = 1
    for song in artista.songs:
        print(i, ". ", song.name)
        i += 1
    op = 0
    while op != 2:
        print("\n1. Seleccionar cancion")
        print("2. Regresar")
        try:
            op = int(input())
            if op == 1:
                song = select_song(artista.songs)
                if song is not None:
                    return song
                else:
                    return None
            elif op == 2:
                return None

        except ValueError:
            print("Por favor, introduce un número válido.")


def select_song(songs_list):
    n_song = int(input("Ingrese el numero de la cancion que desea ver: "))
    if songs_list:
        if n_song <= len(songs_list) or n_song <= 0:
            song = songs_list[n_song - 1]
            print()
            print(song)
            return song
    return None


def add_to_playlist(user, song):
    print("\n1. Agregar cancion a playlist")
    print("2. Regresar")
    try:
        op = int(input())
        match op:
            case 1:
                i = 1
                for playlist in user.playlists:
                    print(str(i) + ". " + playlist.name)
                    i += 1
                n_playlist = int(input("Ingrese el numero de la playlist a la que desea agregar la cancion: "))
                playlist = user.playlists[n_playlist - 1]
                playlist.addSong(song)
                print("Cancion agregada correctamente.")
    except ValueError:
        print("Por favor, introduce un número válido.")


def playlists(user):
    while True:
        i = 1
        print("\nTus playlists:")
        for playlist in user.playlists:
            print(str(i), ". ", playlist)
            i += 1
        print("\n1. Ver playlist")
        print("2. Agregar playlist")
        print("3. Buscar cancion en playlist")
        print("4. Regresar")
        try:
            op = int(input())
            match op:
                case 1:
                    if user.playlists:
                        n_playlist = int(input("Ingrese el numero de la playlist que quiere ver: "))
                        playlist = user.playlists[n_playlist - 1]
                        if playlist.songs:
                            sort_playlist(playlist)
                            show_songs(playlist)
                        else:
                            print("La lista esta vacia.")
                    else:
                        print("No hay playlists guardadas.")
                case 2:
                    name = input("Ingrese el nombre de la playlist: ")
                    new_playlist = Playlist(name, user)
                    new_playlist.createPlaylistCsv()
                    print("La playlist " + name + " ha sido creada correctamente.")
                case 3:
                    n_playlist = int(input("Ingrese el numero de la playlist en la que quiere buscar: "))
                    playlist = user.playlists[n_playlist - 1]
                    searching = str(input("Buscar: "))
                    searched_song = search(playlist.songs, searching)
                    if searched_song != -1:
                        print("La cancion se encuentra en la playlist.")
                    else:
                        print("La cancion no se encuentra en la playlist")
            if op == 4:
                break
        except ValueError:
            print("Por favor, introduce un número válido.")


def sort_playlist(playlist):
    print("Ordenar por: ")
    print("1. Artista")
    print("2. Nombre")
    print("3. Año")
    try:
        op = int(input())
        match op:
            case 1:
                playlist.playlistSort("artist")
            case 2:
                playlist.playlistSort("name")
            case 3:
                playlist.playlistSort("year")
    except ValueError:
        print("Por favor, introduce un número válido.")


def add_songs(user, new_path):
    print("Agregue las canciones que desea agregar a la carpeta New.")
    new_songs = readSongsDirectory(new_path)
    for song in new_songs:
        artists = read_artist_csv(user)
        artist = artists.search(artists.root, song.artist)
        if artist is None:
            os.mkdir(user.path + song.artist)
            with open(user.path + 'artists.csv', 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([song.artist])
            artist = Artist(song.artist, user)
        artist.songs = readSongsDirectory(artist.path)
        old_file = new_path + "\\" + song.file_name
        new_file = user.path + song.artist + '\\' + song.artist + " - " + song.name + '.mp3'
        if os.path.isfile(new_file):
            print("La cancion ya esta en la biblioteca.")
            os.remove(old_file)
        else:
            os.rename(old_file, new_file)
