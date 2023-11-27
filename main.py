from usersGraph import *
from user import *
from social import *
import os

if __name__ == '__main__':
    users = readUsersCsv()
    usersGraph = readGraphCsv()
    usersGraph.read_edges(users)
    new_path = os.getcwd() + "\\New"
    usersList = users.getNodes(users.root)

    for user in usersList:
        user.readUserPlaylists(users)
    
    while True:
        print("\nBienvenido")
        print("1. Iniciar sesion")
        print("2. Crear cuenta")
        print("3. Salir")
        try:
            op = int(input())
            match op:
                case 1:
                    currentUser = login(users)
                    artists = read_artist_csv(currentUser)
                    if not os.path.isdir(new_path):
                        os.mkdir(new_path)
                    while True:
                        print("\nMenu")
                        print("1. Ver perfil") 
                        print("2. Tu biblioteca")
                        print("3. Social")
                        print("4. Cerrar sesion")
                        try:
                            opcion = int(input())
                            match opcion:
                                case 1:
                                    print("\nTu perfil:")
                                    currentUser.profile()
                                case 2:
                                    tu_biblioteca(currentUser, artists, new_path)
                                case 3:
                                    social(currentUser, usersGraph, users)
                            if opcion == 4:
                                print("Cerrando sesion")
                                break
                        except ValueError:
                            print("Por favor, introduce un número válido.")
                case 2:
                    print("Crear tu cuenta")
                    newUser = signUp(users)
                    if newUser is not None:
                        users.insert(users.root, NodeTree(newUser.name, newUser))
                        usersGraph = Graph(usersGraph.numNodes+1, usersGraph.numEdges) 
                        usersGraph.read_edges(users)

            if op == 3:
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
