from biblioteca import *
from graph import *

root_path = os.getcwd()

def social(user, usersGraph, users):
    while True:
        print("\nSocial")
        print("1. Ver seguidos")
        print("2. Ver seguidores")
        print("3. Explorar")
        print("4. Regresar")
        try:
            option = int(input())
            if option == 1:
                if user.following:
                    for follow in user.following:
                        print(follow.name)
                else:
                    print("No se encontraron usuarios")
            elif option == 2:
                if user.followers:
                    for follower in user.followers:
                        print(follower.name)
                else:
                    print("No se encontraron usuarios")
            elif option == 3:
                explore(user, usersGraph, users)
            elif option == 4:
                break     
            else:
                raise ValueError
        except ValueError:
            print("Por favor, introduce un número válido.")


def explore(user, usersGraph, users):
    while True:
        closeUsers = usersGraph.breadth_first_search(user)
        if closeUsers:
            print("Personas que quiza conozcas: ")
            for user1 in closeUsers:
                print(user1.name)
        print("1. Buscar")
        print("2. Regresar")
        try:
            option = int(input())
            if option == 1:
                    search(user, usersGraph, users)
            elif option == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Por favor, introduce un número válido.")
        

def searchUser(users):
    userName = str(input("Ingrese el nombre del usuario "))
    searchedUser = users.search(users.root, userName)
    return searchedUser


def search(user, usersGraph, users):
    searchedUser = searchUser(users)
    if searchedUser is None:
        print("El usuario no ha sido encontrado")
    else:
        searchedUser.profile()
        while True:
            print("\n1. Seguir a ", searchedUser.name)
            print("2. Ver playlists de ", searchedUser.name)
            print("3. Salir")
            try:
                option = int(input())
                if option == 1:
                    if user in searchedUser.followers:
                        print("Ya sigues a este usuario")
                    else:
                        follow(user, usersGraph, users)
                elif option == 2:
                    if user in searchedUser.followers:
                        playlistSearchedUser(searchedUser)
                    else:
                        print("Debes de seguir a esta usuario para ver sus playlist")
                elif option == 3:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, introduce un número válido.")

def follow(user, usersGraph, users):
    usersGraph = Graph(usersGraph.numNodes, usersGraph.numEdges+1)
    usersGraph.insert_edge(user, searchedUser)
    usersGraph.read_edges(users)
    addFriend(user, searchedUser)
    searchedUser.followers.append(user)


def playlistSearchedUser(searchedUser):
    if not searchedUser.playlists:
        print("El usuario no tiene playlists guardadas.")
    else:
        i = 1
        for playlist in searchedUser.playlists:
            print(i, ". ", playlist)
            i += 1
        while True:
            print("1. Ver playlist")
            print("2. Regresar")
            try:
                op = int(input())
                match op:
                    case 1:
                        nPlaylist = int(input("Ingrese el numero de la playlist que quiere ver: "))
                        playlist = searchedUser.playlists[nPlaylist - 1]
                        show_songs(playlist)
                if op == 2:
                    break
            except ValueError:
                print("Por favor, introduce un número válido.")


def addFriend(user, searchedUser):
    modified_lines = []
    with open(root_path + "\\Users\\users_graph.csv", 'r', newline='') as archivo:
        lector_csv = csv.reader(archivo)
        for linea in lector_csv:
            if linea[0] == user.name:
                linea.append(searchedUser.name)
            modified_lines.append(linea)

    with open(root_path + "\\Users\\users_graph.csv", 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(modified_lines)
