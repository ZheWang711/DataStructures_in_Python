__author__ = 'WangZhe'


class Node:
    __slots__ = 'id', 'shortest_distance', 'explored'

    def __init__(self, id):
        self.id = id
        self.shortest_distance = float('inf')
        self.explored = False

    def __str__(self):
        return 'id: {0}, distance: {1}, explored: {2}'.format(self.id, self.shortest_distance, self.explored)


class Edge:
    __slots__ = 'v1', 'v2', 'weight'

    def __init__(self, v1, v2, w):
        self.v1 = v1
        self.v2 = v2
        self.weight = w

    def __str__(self):
        return 'v1: {0}, v2: {1}, weight {3}'.format(self.v1.id, self.v2.id, self.weight)


class Graph:

    def __init__(self):
        self.outgoing = {}      # [id1][id2] to edge object
        self.incoming = {}    # [id2][id1] to edge object
        self.vertices = {}      # id to vertex object

    def insert_vertex(self, id):
        self.vertices[id] = Node(id)
        self.incoming[id] = {}
        self.outgoing[id] = {}

    def insert_edge(self, id1, id2, w):
        tmp = Edge(self.vertices[id1], self.vertices[id2], w)
        self.outgoing[id1][id2] = tmp
        self.incoming[id2][id1] = tmp

    def dijkstra(self, s):
        X = [s.id]     # explored vertices id

        A = [float('inf') for i in range(len(self.vertices) + 1)]        # computed shortest path
        A[s.id] = 0

        in_X = [False for i in range(len(self.vertices) + 1)]   # in_X[id] = True if id is in X
        in_X[s.id] = True
        num_of_vertices = len(self.vertices)

        while len(X) < num_of_vertices:
            tmp1 = None
            tmp2 = None  # temporary vertex 2
            min_value = float('inf')
            for i in X:
                for j in self.outgoing[i].keys():
                    if not in_X[j] and A[i] + self.outgoing[i][j].weight < min_value:
                        min_value = self.outgoing[i][j].weight + A[i]
                        tmp1 = i
                        tmp2 = j
            in_X[tmp2] = True
            A[tmp2] = min_value
            X.append(tmp2)
        return A[1:]


class Solution:
    def __init__(self):
        distances = self.construct(length=200, filename='dijkstraData.txt')
        for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
           print(distances[i-1], end=',')


    def construct(self, length, filename):
        G = Graph()
        for i in range(1, length + 1):
            G.insert_vertex(i)

        file = open(filename, 'r')
        for i in file:
            i = i.replace('\t', ' ').replace(',', ' ')
            buffer = i.split()
            data = [int(i) for i in buffer]
            i = 1
            while i < len(data):
                G.insert_edge(data[0], data[i], data[i + 1])
                i += 2
        return G.dijkstra(G.vertices[1])


if __name__ == '__main__':
    Solution()