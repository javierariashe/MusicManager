from user import *
from graph import *

root_path = os.getcwd() + "\\Users\\"


def contar_lineas_csv():
    file = root_path + 'users_graph.csv'
    try:
        with open(file, 'r') as archivo:
            cantidad_lineas = len(archivo.readlines())
            return cantidad_lineas
    except FileNotFoundError:
        print(f"El archivo {file} no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None


def contar_total_columnas_csv():
    file = root_path + 'users_graph.csv'
    try:
        with open(file, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            cantidad_columnas = 0
            for fila in lector_csv:
                cantidad_columnas += len(fila)-1
            return cantidad_columnas
    except FileNotFoundError:
        print(f"El archivo {file} no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None


def readGraphCsv():
    numNodes = contar_lineas_csv()
    numEdges = contar_total_columnas_csv()
    usersGraph = Graph(numNodes, numEdges)
    return usersGraph
