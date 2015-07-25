__author__ = 'WangZhe'
import random
import copy
"""
The Graph ADT
* Vertex: light weight object that store an arbitrary element, provided by the user
    ** element(): to retrieve the stored element
* Edge: also stores an associated object
    ** element(): to retrieve the stored element
    ** endpoints(): return a tuple such that vertex u is the origin of the edge and the vertex v is the destination
    ** opposite(v): assuming vertex v is one endpoint of the edge (origin or destination), return other endpoint
* Graph:
    ** vertex_count(): return the number of vertices of the graph
    ** vertices(): return an iteration of all the vertices of the graph
    ** edge_count(): return the number of edges of the graph
    ** edges(): return an iteration of all the edges of the graph
    ** get_edge(u, v): return the edge from vertex to vertex v (if exists); otherwise return None
    ** degree(v, out=True): for undirected graph, return the number of edges incident to vertex v.
                            for directed graph, return the number of outgoing edges incident to v.
    ** incident_edges(v, out=True): return an iteration of of all edges incident to vertex v.
                                    In the case of a directed graph, report outgoing edges by default; report incoming
                                    edges if optional parameter is set to False
    ** insert_vertex(x=None): Create and return a new Vertex storing element x
    ** insert_edge(u, v, x=None): Create and return a new Edge from vertex u to vertex v, storing element x (None by
    default)
    ** remove_vertex(v): remove vertex v and all its incident edges from the graph
    ** remove_edge(e): Remove edge e from the graph
"""


# --------------------------nested Vertex class-------------------
class Vertex:
    """ Lightweight vertex structure for a graph. """
    __slots__ = '_element'

    def __init__(self, x):
        """
        Do not call constructor directly. Use Graph's insert_vertex(x).
        """
        self._element = x

    def element(self):
        """
        Return element associated with this vertex
        """
        return self._element

    def __hash__(self):     # will allow vertex to be a map/set key
        return hash(id(self))

    def __str__(self):
        return self._element


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


class Graph:
    """
    Representation of a simple graph using an adjacency map
    The inner representation is a dictionary of dictionaries
    The outer dictionary: key is vertex, value is its corresponding dictionary maintaining its edges
    The inner dictionary: key is another vertex, value is the edges
    """
    def __init__(self, directed=False):
        """
        Create an empty graph(undirected by default)

        Graph is directed if optional parameter is set to True
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """
        :return: Return True if this is a directed graph; False if undirected
        Property is based on the original declaration of the graph, not its contents
        """
        return self._incoming is not self._outgoing     # directed if maps are distinct

    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph"""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(sum(self._outgoing[v][k]._element for k in self._outgoing[v].keys()) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges in the graph"""
        result = set()
        for i in self._outgoing:
            result.update(self._outgoing[i].values())
        return result

    def get_edge(self, u, v):
        """return the edge from u to v, None if not adjacent"""
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """
        :param v: vertex.
        :param outgoing: if true, calculating outgoing degree, else calculating incoming degree
        :return: return the number of edges incident to vertex v in the graph
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """
        Returning all outgoing (incoming) edges of a given vertex v
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """
        Insert a vertex u whose element is x, and return the new vertex
        """
        u = Vertex(x)
        self._outgoing[u] = {}
        if self.is_directed():
            self._incoming[u] = {}
        return u

    def insert_edge(self, u, v, x=1):
        """
        Insert a new edge (u, v) with element x, and return the new edge
        """
        edge = Edge(u, v, x)
        self._outgoing[u][v] = edge
        self._incoming[v][u] = edge
        return edge

    # TODO: remove_vertex() and remove_edge() need to be tested
    def remove_vertex(self, v):
        """
        Delete and return the vertex v, also delete its related egdes
        """
        del self._outgoing[v]   # TODO: check memory leak ??
        for secondary_map in self._outgoing.values():
            if secondary_map.get(v) is not None:
                del secondary_map[v]
        if self.is_directed():
            del self._incoming[v]   # TODO: check memory leak ??
            for secondary_map in self ._incoming.values():
                if secondary_map.get(v) is not None:
                    del secondary_map[v]

    def remove_edge(self, u, v):
        if self.get_edge(u, v) is None:
            return
        del self._incoming[v][u]
        del self._outgoing[u][v]

    def display(self):
        print("outgoing")
        for origin in self._outgoing.keys():
            print(origin, end=': ')
            for destination in self._outgoing[origin].keys():
                print(self._outgoing[origin][destination], end=' || ')
            print()
        if self.is_directed():
            print("incoming")
            for destination in self._incoming.keys():
                print(destination, end=': ')
                for origin in self._incoming[destination].keys():
                    print(self._incoming[destination][origin], end=' || ')
                print()

    def insert_multiple_edges(self, u, v, x=1):
        """insert a multiple edge, supports only undirected graphs"""
        if not self._outgoing[u].get(v):
            self.insert_edge(u, v, x)
        else:
            self._outgoing[u][v]._element += x
            self._incoming[v][u]._element = self._outgoing[u][v]._element

    def remove_multiple_edge(self, u, v, x=1):
        if self._outgoing[u][v]._element == x:
            self.remove_edge(u, v)
        else:
            self._outgoing[u][v]._element -= x
            self._incoming[v][u]._element = self._outgoing[u][v]._element

    def merge_vertex(self, u, v):
        newvertex = self.insert_vertex(u._element + v._element)
        for dest, edge in self._outgoing[u].items():
            if dest == v:
                continue
            self.insert_multiple_edges(newvertex, dest, edge._element)
        for dest, edge in self._outgoing[v].items():
            if dest == u:
                continue
            self.insert_multiple_edges(newvertex, dest, edge._element)
        self.remove_vertex(u)
        self.remove_vertex(v)
        return newvertex

    def random_contraction_algorithm(self):
        """
        Minimum Cut problem
        due to Karger, earlier 90s
        Reference: https://d396qusza40orc.cloudfront.net/algo1/slides/algo-karger-algorithm_typed.pdf
        """
        if self.vertex_count() == 2:
            return self.edge_count()
        times = self.vertex_count() ** 3
        min = [float("inf")]
        V = [Vertex('pos1'), Vertex('pos2')]
        for i in range(times):
            tmp = copy.deepcopy(self)
            vertices_list = list(tmp.vertices())
            while tmp.vertex_count() > 2:
                v1 = random.choice(vertices_list)
                vertices_list.remove(v1)
                v2 = random.choice(vertices_list)
                vertices_list.remove(v2)
                v3 = tmp.merge_vertex(v1, v2)
                vertices_list.append(v3)
            if tmp.edge_count() < min[0]:
                min[0] = tmp.edge_count()
                index = 0
                for vertex in tmp.vertices():
                    V[index] = vertex
                    index += 1
        return min[0], V

if __name__ == '__main__':
    # undirected
    g = Graph(directed=False)
    u = g.insert_vertex('u')
    v = g.insert_vertex('v')
    w = g.insert_vertex('w')
    z = g.insert_vertex('z')
    g.insert_multiple_edges(u, v)
    g.insert_multiple_edges(v, w)
    g.insert_multiple_edges(u, w)
    g.insert_multiple_edges(w, z)
    g.insert_multiple_edges(w, z)
    count, V = g.random_contraction_algorithm()
    print(count)
    for i in V:
        print(i._element)
