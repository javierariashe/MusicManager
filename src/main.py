from usersGraph import *
from user import *
from social import *
import os

def menu_login():
    user = login(users)
    artists = read_artist_csv(user)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    return user, artists

def menu_create():
    newUser = None
    while not newUser:
        newUser = signUp(users)

    if newUser:
        users.insert(users.root, NodeTree(newUser.name, newUser))
        usersGraph = Graph(usersGraph.numNodes+1, usersGraph.numEdges) 
        usersGraph.read_edges(users)

    return newUser

if __name__ == '__main__':
    users = readUsersCsv()
    usersGraph = readGraphCsv()
    usersGraph.read_edges(users)
    new_path = os.getcwd() + "\\New"
    usersList = users.getNodes(users.root)
    currentUser = None

    for user in usersList:
        user.readUserPlaylists(users)
    
    while not currentUser:
        print("\nBienvenido")
        print("1. Iniciar sesion")
        print("2. Crear cuenta")
        print("3. Salir")
        try:
            option = int(input())
            if option == 1:
                currentUser, userArtists = menu_login()
            elif option == 2:
                print("---Crea tu cuenta---")
                currentUser = menu_create()
            elif option == 3:
                break

            else:
                raise ValueError

        except ValueError:
            print("Por favor, introduce un número válido.")

    while currentUser:
        print("\nMenu")
        print("1. Ver perfil") 
        print("2. Tu biblioteca")
        print("3. Social")
        print("4. Cerrar sesion")
        try:
            option = int(input())
            if option == 1:
                myProfile(currentUser)
            elif option == 2:
                tu_biblioteca(currentUser, userArtists, new_path)
            elif option == 3:
                social(currentUser, usersGraph, users)
            elif option == 4:
                currentUser = None
                print("Cerrando sesion.")
            else:
                raise ValueError

        except ValueError:
            print("Por favor, introduce un número válido.")