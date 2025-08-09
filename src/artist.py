import csv
from song import *
from binarytree import *


class Artist:
    def __init__(self, name, user):
        self.name = name
        self.path = user.path + name
        self.songs = readSongsDirectory(self.path)


def read_artist_csv(user):
    artists = BT()
    with open(user.path + 'artists.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            artists.insert(artists.root, NodeTree(row[0], Artist(row[0], user)))
            line += 1
    return artists
