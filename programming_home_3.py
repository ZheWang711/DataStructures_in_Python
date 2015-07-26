__author__ = 'WangZhe'
import random
# --------------------------nested Edge class-----------------------
class Edge:
    """
    Lightweight edge structure for a graph.
    """
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """Return (u, v) tuple for vertices u and v"""
        return self._origin, self._destination

    def opposite(self, v):
        """Return the vertex that is opposite v on this edge"""
        return self._destination if v is self._origin else self._origin

    def element(self):
        return self._element

    def __hash__(self):     # will allow edge to be a map/set key
        return hash((self._origin, self._destination))

    def __str__(self):
        return '(' + str(self._origin) + ',' + str(self._destination) + ',' + str(self._element) + ')'


class UndirectedGraph:
    """
    An highly customized graph data structure for the running of Karger's Minimum Cut problem
    Reference https://d396qusza40orc.cloudfront.net/algo1/slides/algo-karger-analysis_typed.pdf
    Optimizing the "Merge Vertices" behaviour by introducing Set
    """
    def __init__(self):
        self._outgoing = [None] * 300
        self._ver_num = 0
        self._edge_num = 0

    def insert_vertex(self, x):
        # without check if the vertex already exists
        self._outgoing[x] = {}
        self._ver_num += 1

    def insert_edge(self, x, y):
        self._outgoing[x][y] = Edge(x, y, 1)
        self._edge_num += 1

    def get_edge(self, x, y):
        return self._outgoing[x].get(y)

    def get_neighbour_verticves(self, x):
        for y in self._outgoing[x].keys():
            yield y

    def edge_count(self):
        return self._edge_num // 2

    def main(self, filename):
        f = open(filename, 'r')
        input_list = []
        for line in f:
            input_list.append([int(s) for s in line.split()])
        f.close()
        for i in range(len(input_list)):
            self.insert_vertex(i + 1)
        for i in range(1, self._ver_num + 1):   # i is the origin
            for dest in input_list[i - 1]:
                if dest == i:
                    continue
                else:
                    if self.get_edge(i, dest) is not None:
                        continue
                    self.insert_edge(i, dest)

    def contraction(self):
        # For randomized choice
        li = [i for i in range(1, self._ver_num + 1)]

        # In each iteration, the value subtracts the number of edges that is "merged" into sets, i.e.
        # the edges(u, v) that are swallowed into the larger vertices (sets)
        # After finishing all iterations, "result" will be the number of edges crossing the two existing sets/vertices
        result = self.edge_count()

        for i in range(self._ver_num - 2):
            p1 = random.choice(li)
            li.remove(p1)
            p2 = random.choice(li)
            li.remove(p2)
            if type(p1) == int and type(p2) == int:
                if self.get_edge(p1, p2) is not None:
                    result -= 1
                s = {p1, p2}
                li.append(s)
            if type(p1) == set and type(p2) == set:
                for i in p1:
                    for j in self.get_neighbour_verticves(i):
                        if j in p2:
                            result -= 1
                s = p1 | p2
                li.append(s)
            if type(p1) == set and type(p2) == int:
                for i in self.get_neighbour_verticves(p2):
                    if i in p1:
                        result -= 1
                s = p1 | {p2}
                li.append(s)
            if type(p1) == int and type(p2) == set:
                for i in self.get_neighbour_verticves(p1):
                    if i in p2:
                        result -= 1
                s = {p1} | p2
                li.append(s)
        return result

    def Karger_min_cut(self):
        min = float("inf")
        for i in range(self._ver_num ** 2):
            tmp = self.contraction()
            if tmp < min:
                min = tmp
                print(min)
        return min




def main():
    a = UndirectedGraph()
    a.main('KargerMinCut.txt')
    print(a.Karger_min_cut())

main()