__author__ = 'WangZhe'
import sys
import threading


class Node:
    __slots__ = 'id', 'explored'

    def __init__(self, id):
        self.id = id
        self.explored = False

    def __str__(self):
        return str(self.id)


class Edge:
    __slots__ = 'v1', 'v2'

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return '{0} --> {1}'.format(self.v1.id, self.v2.id)


class Graph:

    def __init__(self):
        self.outgoing = {}
        self.incoming = {}
        self.vertices = {}

    def insert_ver(self, id):
        self.vertices[id] = Node(id)
        self.outgoing[id] = {}
        self.incoming[id] = {}

    def insert_edge(self, id1, id2):
        edge = Edge(self.vertices[id1], self.vertices[id2])
        self.outgoing[id1][id2] = edge
        self.incoming[id2][id1] = edge

    def DFS_r(self, start_id):
        self.vertices[start_id].explored = True
        for i in self.incoming[start_id].keys():
            if not self.vertices[i].explored:
                self.DFS_r(i)
        self.order[self.t] = start_id
        self.t += 1

    def DFS(self, start_id):
        self.vertices[start_id].explored = True
        self.leaders[start_id] = self.leader
        for i in self.outgoing[start_id].keys():
            if not self.vertices[i].explored:
                self.DFS(i)

    def SCC(self):
        self.leaders = [None for i in range(len(self.vertices) + 1)]    #leader[id]=lead_id
        self.order = [None for i in range(len(self.vertices) + 1)]      #order[order] = id
        self.t = 1
        self.leader = None  # leader_id

        for i in range(1, len(self.vertices) + 1):
            if not self.vertices[i].explored:
                self.DFS_r(i)

        for i in self.vertices.values():
            i.explored = False

        for i in range(len(self.order) - 1, 0, -1):
            if not self.vertices[self.order[i]].explored:
                self.leader = self.order[i]
                self.DFS(self.order[i])

        return self.leaders

    def final_result(self):
        leaders = self.SCC()
        buffer = {}
        for i in range(1, len(leaders)):
            if buffer.get(leaders[i]) is None:
                buffer[leaders[i]] = 1
            else:
                buffer[leaders[i]] += 1
        l = [i for i in buffer.values()]
        l = sorted(l, key=lambda x: -x)
        print(l[0:5])

class Solution:

    def __init__(self):
        G = self.construct('SCC.txt', 875714)
        G.final_result()

    def construct(self, filename, length):
        G = Graph()
        for i in range(1, length + 1):
            G.insert_ver(i)
        file = open(filename, 'r')
        for line in file:
            x, y = line.split()
            G.insert_edge(int(x), int(y))
        return G

def scc():
    Solution()

if __name__ == '__main__':
    #set rescursion limit and stack size limit, otherwise we will encounter RuntimeError: maximum recursion depth exceeded
    sys.setrecursionlimit(10 ** 6)
    threading.stack_size(267000000)
    thread = threading.Thread(target = scc)
    thread.start()
