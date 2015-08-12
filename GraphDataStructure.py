__author__ = 'WangZhe'
import queue
import random


class Node:
    __slots__ = 'element', 'is_explored', 'id', 'level', 'mark', 'leader'

    def __init__(self, is_explored=False, element=None, id=None, mark=None):
        self.is_explored = is_explored
        self.element = element
        self.id = id
        self.level = 0
        self.mark = 0       # 0 unexplored, 1 explored, -1 in queue/stack
        self.leader = None  # computing SSC, leader vertex

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
        self.current_label = None
        self.label = {}
        # Computing SCC
        self.scc_order = []
        self.finish_time = -1

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
        source.explore()
        while not Q.empty():
            head = Q.get()
            list_to_explore = list(self.outgoing[head].keys()) if self.outgoing[head].keys() is not None else []
            random.shuffle(list_to_explore)
            for i in list_to_explore:
                if not i.is_explored:
                    i.level = head.level + 1
                    i.explore()
                    Q.put(i)

    def Ver(self, id):
        return self.ver[id]

    def insert_edge_by_Ver_id(self, id1, id2, element=None):
        self.insert_edge(self.ver[id1], self.ver[id2], element)

    def insert_undirected_edge(self, id1, id2, element=None):
        self.insert_edge(self.ver[id1], self.ver[id2], element)
        self.insert_edge(self.ver[id2], self.ver[id1], element)

    def connecting_components(self):
        cnt = 1
        for i in self.outgoing.keys():
            if not i.is_explored:
                print("component {0}".format(cnt))
                self.BFS(i)
                cnt += 1

    def DFS(self, source):
        """
        Depth first search using stack
        """
        source.no_level_explore()
        S = [source]    # outer layer explored vertices
        while len(S) != 0:
            vertex = S.pop()
            neighbour_list = list(self.outgoing[vertex].keys()) if self.outgoing[vertex].keys() is not None else []
            random.shuffle(neighbour_list)
            for i in self.outgoing[vertex].keys():
                if not i.is_explored:
                    i.no_level_explore()
                    S.append(i)

    def DFS_r(self, source):
        """
        Depth first search recursive implementation
        """
        source.no_level_explore()
        for i in self.outgoing[source].keys():
            if not i.is_explored:
                self.DFS_r(i)

    def DFS_topo(self, start):
        """
        Depth first search for topological sorting. ( editing self.label )
        """
        start.is_explored = True
        for i in self.outgoing[start].keys():
            if not i.is_explored:
                self.DFS_topo(i)
        self.label[start] = self.current_label
        self.current_label -= 1

    def reverse_DFS(self, start):
        """
        Depth first search for computing SCCs, which searches on reversed version of the graph
        """
        if start.is_explored:
            return
        else:
            start.is_explored = True
            for each_vertex in self.incoming[start].keys():
                if not each_vertex.is_explored:
                    self.reverse_DFS(each_vertex)
            self.scc_order[self.ver_cnt - self.finish_time - 1] = start.id
            self.finish_time += 1

    def DFS_SCC(self, start, current_leader):
        """
        Depth first search for computing SCCs. ( assigning leaders )
        """
        if start.is_explored:
            return
        else:
            start.is_explored = True
            start.leader = current_leader
            for each_vertex in self.outgoing[start].keys():
                if not each_vertex.is_explored:
                    self.DFS_SCC(each_vertex, current_leader)

    def recover(self):
        for i in self.ver:
            self.Ver(i).leader = None
            self.Ver(i).is_explored = False
            self.Ver(i).mark = 0
            self.Ver(i).level = 0
            self.current_label = len(self.outgoing) - 1
            self.label = {v: None for v in self.outgoing.keys()}

    def topological_sort(self):
        self.recover()
        self.current_label = len(list(self.outgoing)) - 1
        to_explore = list(self.outgoing.keys())
        random.shuffle(to_explore)
        for i in to_explore:
            if not i.is_explored:
                self.DFS_topo(i)

    def strong_connecting_components(self):
        self.scc_order = [None for i in range(self.ver_cnt)]    # scc_order[order] = id
        self.finish_time = 0                                    # order = ver_cnt - finish_time
        for i in self.outgoing.keys():
            self.reverse_DFS(i)
        self.recover()
        for i in self.scc_order:
            self.DFS_SCC(self.Ver(i), self.Ver(i))
        for i in self.outgoing.keys():
            print("{0} in group {1}".format(i.id, i.leader.id))


if __name__ == "__main__":
    g = Graph()
    for i in range(1, 12):
        g.insert_ver(Node(id=i))
    edges = [
        (1, 3), (3, 2), (2, 1), (3, 5), (3, 9),
        (1, 4), (4, 6), (4, 10),
        (6, 8), (8, 10), (10, 6),
        (5, 10), (7, 8), (5, 7), (7, 11), (11, 9), (9, 5), (5, 11)

    ]
    for i, j in edges:
        g.insert_edge_by_Ver_id(i, j)
    g.strong_connecting_components()
