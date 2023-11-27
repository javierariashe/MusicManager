import csv
from binarytree import NodeTree, BT
from playlist import *

root_path = os.getcwd() + "\\Users\\"


class User:
    
    def __init__(self, name, password, number):
        self.name = name
        self.password = password
        self.id = int(number)
        self.path = root_path + self.name + "\\"
        self.followers = []
        self.following = []
        self.playlists = []
        
    def validatePassword(self, password):
        if self.password == password:
            return True 
        return False
    
    def follow(self, username, users, usersGraph):
        user = users.search(username)
        self.following.append(user)
        user.followers.append(self)
        usersGraph.insert_edge(self, user)
        
    def profile(self):
        print(self.name)
        print("Seguidores", len(self.followers), "Seguidos", len(self.following))
        
    def readUserPlaylists(self, users):
        path = self.path + "Playlists"
        playlists = []
        playlistsFiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for playlist in playlistsFiles:
            playlist_path = path + "\\" + playlist
            playlists.append(readPlaylistCsv(playlist_path, users))
        self.playlists = playlists


def createUser(name, password):
    with open(root_path + 'users.csv', 'r') as file:
        n = len(file.readlines()) + 1
    newUser = User(name, password, n)
    with open(root_path + 'users.csv', 'a', newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow([name, password, n])
    with open(root_path + 'users_graph.csv', 'a', newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow([name])
    try:
        os.mkdir(newUser.path)
        os.mkdir(newUser.path + "\\Playlists")
        open(newUser.path + 'artists.csv', 'w')
    finally:
        return newUser


def login(users):
    validUser = False
    validPassword = False
    user = None
                
    while not validUser:
        username = input("Usuario: ")
        user = users.search(users.root, username)
        if user is not None:
            validUser = True
        else:
            print("Usuario no encontrado.")

    while not validPassword:
        password = input("Contrasena: ")
        validPassword = user.validatePassword(password)
        if not validPassword:
            print("Contrasena incorrecta.")
    print("\nSesion iniciada correctamente." + " Usuario: " + user.name)
    return user  


def signUp(users):
    name = input("Ingresa tu nombre de usuario: ")
    if users.search(users.root, name) is None:
        password = input("Ingresa tu contraseña: ")
        newUser = createUser(name, password)
        return newUser

    else:
        print("Nombre de usuario no disponible")
        return None


def readUsersCsv():
    users = BT()
    with open(root_path + 'users.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            users.insert(users.root, NodeTree(row[0], User(row[0], row[1], row[2])))
            line += 1
    return users
