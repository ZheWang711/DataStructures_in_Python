__author__ = 'WangZhe'
import queue
import random

class Node:
    __slots__ = 'element', 'is_explored', 'id', 'level', 'mark'

    def __init__(self, is_explored=False, element=None, id=None, mark=None):
        self.is_explored = is_explored
        self.element = element
        self.id = id
        self.level = 0
        self.mark = 0 # 0 unexplored, 1 explored, -1 in queue/stack

    def __str__(self):
        return "vertex {0}: {1}".format(self.id, self.element)

    def __hash__(self):
        return hash(self.id)

    def explore(self):
        self.is_explored = True
        self.mark = 1
        print("exploring {0} in level {1}".format(self.id, self.level))

    def no_level_explore(self):
        self.is_explored = True
        self.mark = 1
        print("exploring {0}".format(self.id))

class Edge:
    __slots__ = 'v1', 'v2', 'element'

    def __init__(self, v1, v2, element=None):
        self.v1 = v1
        self.v2 = v2
        self.element = element

    def __str__(self):
        return "Edge {0} connecting {1} with {2}".format(self.element, self.v1, self.v2)

    def __hash__(self):
        return hash((self.v1, self.v2))


class Graph:
    def __init__(self):
        self.ver = {}
        self.outgoing = {}
        self.incoming = {}
        self.ver_cnt = 0
        self.edge_cnt = 0

    def insert_ver(self, Vertex):
        self.ver[Vertex.id] = Vertex
        self.outgoing[Vertex] = {}
        self.incoming[Vertex] = {}
        self.ver_cnt += 1

    def insert_edge(self, V1, V2, element=None):
        self.edge_cnt += 1
        new_edge = Edge(V1, V2, element)
        self.outgoing[V1][V2] = new_edge
        self.incoming[V2][V1] = new_edge

    def get_all_outgoing(self, v1):
        if self.outgoing.get(v1) is None:
            raise ValueError("No such vertex {0}".format(v1))
        else:
            return self.outgoing[v1].keys()

    def get_all_incoming(self, v1):
        if self.incoming.get(v1) is None:
            raise ValueError("No such vertex {0}".format(v1))
        else:
            return self.incoming[v1].keys()

    def BFS(self, source):  # source is the initial vertex (reference)
        Q = queue.Queue()
        Q.put(source)
        while not Q.empty():
            head = Q.get()
            if not head.is_explored:
                head.explore()
                list_to_explore = list(self.outgoing[head].keys()) if self.outgoing[head].keys() is not None else []
                random.shuffle(list_to_explore)
                for i in list_to_explore:
                    if i.mark == 0:     # unexplored
                        i.level = head.level + 1
                        Q.put(i)
                        i.mark = -1     # in queue


    def Ver(self, id):
        return self.ver[id]

    def insert_edge_by_Ver_id(self, id1, id2, element=None):
        self.insert_edge(self.ver[id1], self.ver[id2], element)

    def insert_undirected_edge(self, id1, id2, element=None):
        self.insert_edge(self.ver[id1], self.ver[id2], element)
        self.insert_edge(self.ver[id2], self.ver[id1], element)

    def connecting_compunents(self):
        cnt = 1
        for i in self.outgoing.keys():
            if not i.is_explored:
                print("component {0}".format(cnt))
                self.BFS(i)
                cnt += 1

    def DFS(self, source):
        S = [source]    # nodes to be explored
        while len(S) != 0:
            vertex = S.pop()
            if not vertex.is_explored:
                vertex.no_level_explore()
                neighbour_list = list(self.outgoing[vertex].keys()) if self.outgoing[vertex].keys() is not None else []
                random.shuffle(neighbour_list)
                for i in self.outgoing[vertex].keys():
                    if i.mark == 0:
                        S.append(i)
                        i.mark = -1

    def DFS_r(self, source):
        source.explore()
        for i in self.outgoing[source].keys():
            if not i.is_explored:
                self.DFS_r(i)

    def recover(self):
        for i in self.ver:
            self.Ver(i).is_explored = False
            self.Ver(i).mark = 0




if __name__ == "__main__":
    g = Graph()
    for i in range(1, 11):
        g.insert_ver(Node(id=i))
    g.insert_undirected_edge(1, 3)
    g.insert_undirected_edge(1, 5)
    g.insert_undirected_edge(3, 5)
    g.insert_undirected_edge(5, 7)
    g.insert_undirected_edge(5, 9)
    g.insert_undirected_edge(2, 4)
    g.insert_undirected_edge(6, 8)
    g.insert_undirected_edge(8, 10)
    g.insert_undirected_edge(6, 10)
    g.DFS_r(g.Ver(1))
    g.recover()
    g.DFS_r(g.Ver(1))
    g.recover()
    g.connecting_compunents()
    print('second time')
    g.recover()
    g.connecting_compunents()
    #g.connecting_compunents()