__author__ = 'WangZhe'
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
        return self._origin,  self._destination , self._element


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
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges in the graph"""
        result = set()
        for i in self._outgoing:
            result.update(self._outgoing[i].values())
        return result

    def get_edge(self, u, v):
        """return the edge from u to v, None if not adjacent"""
        return self._outgoing[u].get(v, default=None)

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

    def insert_edge(self, u, v, x):
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
        for secondary_map in self._outgoing:
            if secondary_map.get(v) is not None:
                del secondary_map[v]
        if self.is_directed():
            del self._incoming[v]   # TODO: check memory leak ??
            for secondary_map in self ._incoming:
                if secondary_map.get(v) is not None:
                    del secondary_map[v]

    def remove_edge(self, u, v):
        if self.get_edge(u, v) is None:
            return
        del self._incoming[v][u]
        del self._outgoing[u][v]

    def traverse(self):
        print("outgoing")
        for secondary_map in self._outgoing:
            print(secondary_map, end=': ')
            for edges in secondary_map.values():
                print(edges, end='||||')

def main():
    # undirected
    g = Graph()
    u = g.insert_vertex('u')
    v = g.insert_vertex('v')
    w = g.insert_vertex('w')
    z = g.insert_vertex('z')
    g.insert_edge(u, v, 'e')
    g.insert_edge(v, w, 'f')
    g.insert_edge(u, w, 'g')
    g.insert_edge(w, z, 'h')
    g.traverse()
    print(0)

main()