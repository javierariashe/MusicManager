import os
import csv

root_path = os.getcwd() + "\\Users\\"


class Node:
    to = None
    nxt = None
    prev = None
    color = 0
    distance = -1
    user = None

    def __init__(self, user):
        self.user = user


class Graph:

    def __init__(self, numNodes, numEdges):
        self.numNodes = numNodes
        self.numEdges = numEdges
        self.directed = True
        self.edges = []
        self.grade = []

        i = 0
        while i <= self.numNodes:
            self.grade.append(0)
            self.edges.append(None)
            i += 1

    def insert_edge(self, u, v):
        item = Node(u)
        item.to = v
        item.nxt = self.edges[u.id]

        self.edges[u.id] = item
        self.grade[u.id] += 1

    def read_edges(self, users):
        with open(root_path + 'users_graph.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in csv_reader:
                u = users.search(users.root, row[0])
                if u is not None:
                    for j in range(1, len(row)):
                        v = users.search(users.root, row[j])
                        if v is not None:
                            u.following.append(v)
                            v.followers.append(u)
                            self.insert_edge(u, v)
                    line += 1

    def print(self):
        i = 1
        string = ""
        while i <= self.numNodes:
            string += str(i) + "\t"
            item = self.edges[i]

            while item is not None:
                string += str(item.to.name) + ": " + "\t"
                item = item.nxt

            string += "\n"
            i += 1

        print(string)

    def breadth_first_search(self, intSource):
        if self.edges[intSource.id] is None:
            return None

        for i in range(1, self.numNodes + 1):
            if self.edges[i] is not None:
                self.edges[i].color = 0
                self.edges[i].distance = -1
                self.edges[i].prev = None

        intSource.color = 1
        intSource.distance = 0
        queue = [intSource]
        nodes_two = []

        while queue:
            u = queue.pop(0)
            v = self.edges[u.id]

            while v is not None:
                if self.edges[v.to.id] is not None and self.edges[v.to.id].color == 0:
                    self.edges[v.to.id].color = 1
                    self.edges[v.to.id].distance = self.edges[u.id].distance + 1
                    self.edges[v.to.id].prev = u
                    queue.append(v.to)
                    if self.edges[v.to.id].distance == 1:
                        nodes_two.append(v.to)
                v = v.nxt

            self.edges[u.id].color = 2

        return nodes_two
