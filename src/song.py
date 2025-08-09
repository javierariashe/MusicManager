import os
from pathlib import Path


class Song:
    def __init__(self, name, artist, album, year, file_name):
        self.name = name.replace('?', ' ').strip()
        self.artist = artist.replace('?', ' ').partition('/')[0].partition("feat")[0].partition("ft")[0].strip()
        self.album = album.replace('?', ' ').strip()
        self.year = year.strip()
        self.file_name = file_name

    def __str__(self):
        return ("Nombre: " + self.name + "\nArtista: " + self.artist
                + "\nAlbum: " + self.album + "\nAño: " + self.year)


def readSong(song_file):
    song = None
    try:
        with open(song_file, "rb") as file:
            file.seek(-128, 2)
            tag = file.read(128)
            file_name = Path(file.name).stem + '.mp3'

        if len(tag) == 128 and tag[:3] == b"TAG":
            title = tag[3:33].split(b'\x00', 1)[0].decode("utf-8").strip()
            artist = tag[33:63].split(b'\x00', 1)[0].decode("utf-8").strip()
            album = tag[63:93].split(b'\x00', 1)[0].decode("utf-8").strip()
            year = tag[93:97].decode("utf-8").strip()

            song = Song(title, artist, album, year, file_name)
        else:
            print("No fue posible agregar el archivo " + file_name)
            os.remove(song_file)

    except Exception as e:
        print(f"An error occurred: {e}")

    return song


def readSongsDirectory(path):
    songsList = []
    songFiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for song in songFiles:
        song_path = path + "\\" + song
        songsList.append(readSong(song_path))
    return songsList
