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
            option = int(input())
            if option == 1:
                show_artist(user, artists)
            elif option == 2:
                playlists(user)
            elif option == 3:
                add_songs(user, new_path)
                artists = read_artist_csv(user)
            elif op == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Por favor, introduce un número válido.")


def show_artist(user, artists):
    artist_name = str(input("Ingrese el nombre del artista: "))
    artist = artists.search(artists.root, artist_name)
    if artist is not None:
        while True:
            print("\n1. Ver canciones")
            print("2. Regresar")
            try:
                option = int(input())
                if option == 1:
                    song = show_songs(artist)
                    if song is not None:
                        add_to_playlist(user, song)
                elif option == 2:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, introduce un número válido.")
    else:
        print("El artista no esta en tu biblioteca")


def show_songs(artista):
    print("Canciones:")
    i = 1
    for song in artista.songs:
        print(i, ". ", song.name)
        i += 1
    while True:
        print("\n1. Seleccionar cancion")
        print("2. Regresar")
        try:
            option = int(input())
            if option == 1:
                song = select_song(artista.songs)
                if song is not None:
                    return song
                else:
                    return None
            elif op == 2:
                return None
            else:
                raise ValueError

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
        option = int(input())
        if option == 1:
            i = 1
            for playlist in user.playlists:
                print(str(i) + ". " + playlist.name)
                i += 1
            n_playlist = int(input("Ingrese el numero de la playlist a la que desea agregar la cancion: "))
            playlist = user.playlists[n_playlist - 1]
            playlist.addSong(song)
            print("Cancion agregada correctamente.")
        elif option != 2:
            raise ValueError
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
        print("3. Regresar")
        try:
            option = int(input())
            if option == 1:
                seePlaylist(user)
            elif option == 2:
                createPlaylist(user)
            elif option == 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Por favor, introduce un número válido.")


def sort_playlist(playlist):
    print("Ordenar por: ")
    print("1. Artista")
    print("2. Nombre")
    print("3. Año")
    try:
        option = int(input())
        if option == 1:
            playlist.playlistSort("artist")
        elif option == 2:
            playlist.playlistSort("name")
        elif option == 3:
            playlist.playlistSort("year")
        else:
            raise ValueError
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
