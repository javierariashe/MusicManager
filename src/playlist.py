from user import *
from song import *
from quick import *


class Playlist: 

    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.songs = []
        self.csv = ""
        self.csvName()
        user.playlists.append(self)

    def addSong(self, song):
        self.songs.append(song)
        with open(self.csv, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([song.name, song.artist, song.album, song.year, song.file_name])
        
    def deleteSong(self, song):
        self.songs.remove(song)
        with open(self.csv, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)

        with open(self.csv, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for row in data:
                if song.name == row[0]:
                    continue
                csv_writer.writerow(row) 
        
    def csvName(self):
        path = self.user.path + "\\" + "Playlists\\"
        self.csv = path + self.name + '.csv'   
        
    def createPlaylistCsv(self):
        with open(self.csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.user.name])
        self.csvName()

    def playlistSort(self, type_sort):
        if type_sort == 'artist':
            quickSortArtist(self.songs, 0, len(self.songs) - 1)
        elif type_sort == 'name':
            quickSortName(self.songs, 0, len(self.songs) - 1)
        elif type_sort == 'year':
            quickSortYear(self.songs, 0, len(self.songs) - 1)
            
    def __str__(self):
        return "Playlist: " + self.name + "\tUsuario: " + self.user.name

def seePlaylist(user):
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

def createPlaylist(user):
    name = input("Ingrese el nombre de la playlist: ")
    new_playlist = Playlist(name, user)
    new_playlist.createPlaylistCsv()
    print("La playlist " + name + " ha sido creada correctamente.")

def readPlaylistCsv(path, users):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line == 0:
                user = row[1]
                user = users.search(users.root, user)
                if user is not None:
                    playlist = (Playlist(row[0], user))
            else:
                playlist.songs.append(Song(row[0], row[1], row[2], row[3], row[4]))
            line += 1
    return playlist


def readDirectory(path):
    songsList = []
    songFiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for song in songFiles:
        song_path = path + "/" + song
        songsList.append(readSong(song_path))
    return songsList
