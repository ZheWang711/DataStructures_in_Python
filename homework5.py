__author__ = 'WangZhe'
import heap

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

        A = [float('inf') for i in range(len(self.vertices) + 1)]        # computed shortest path

        in_X = [False for i in range(len(self.vertices) + 1)]   # in_X[id] = True if id is in X

        # initialize heap:
        H = heap.Heap()
        for i in self.vertices.values():
            if i == s:
                H.insert(heap.Data(0, i))
            else:
                H.insert(heap.Data(float('inf'), i))

        for i in range(len(self.vertices)):
            tmp_data = H.extract_min()
            distance, ver = tmp_data.key, tmp_data.value
            in_X[ver.id] = True
            A[ver.id] = distance
            for i in self.outgoing[ver.id].keys():
                if not in_X[i]:
                    tmp_neighbour = H.remove_obj(self.vertices[i])
                    new_distance = min(tmp_neighbour.key, self.outgoing[ver.id][i].weight + distance)
                    H.insert(heap.Data(new_distance, self.vertices[i]))
                    A[i] = new_distance
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