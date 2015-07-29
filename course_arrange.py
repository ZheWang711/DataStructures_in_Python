__author__ = 'WangZhe'
import collections
import copy

class my_queue(collections.deque):
    def get_head(self):
        a = self.pop()
        self.append(a)
        return a

    def out_queue(self):
        return self.pop()

    def in_queue(self, item):
        self.appendleft(item)

    def is_empty(self):
        return len(self) == 0

class Vertex:
    """ Lightweight vertex structure for a graph. """
    __slots__ = '_course_name', '_identifier', 'state'

    def __init__(self, name, id):
        """
        Do not call constructor directly. Use Graph's insert_vertex(x).
        """
        self._course_name = name
        self._identifier = id
        self.state = 0

    def in_queue(self):
        self.state = 1

    def choose(self):
        self.state = 2

    def is_in_queue(self):
        return self.state == 1

    def is_choose(self):
        return self.state == 2

    def is_nothing(self):
        return self.state == 0

    def name(self):
        return self._course_name

    def get_id(self):
        return self._identifier

    def __hash__(self):     # will allow vertex to be a map/set key
        return hash(id(self))

    def __str__(self):
        return str(self._identifier) + ': ' + str(self._course_name)

class Edge:
    __slots__ = 'pre', 'post'

    def __init__(self, c1, c2):
        self.pre = c1
        self.post = c2

    def __str__(self):
        return str(self.pre) + ' --> ' + str(self.post)


class Graph:

    def __init__(self):
        self._outgoing = {}
        self._incoming = {}
        self.coursetable = {}
        self.indegrees = {}
        self.vertexnum = 0

    def vertices(self): #return the id
        for i in self._outgoing.keys():
            yield i

    def insert_vertex(self, id, name=''):
        self._outgoing[id] = {}
        self._incoming[id] = {}
        self.coursetable[id] = Vertex(name, id)
        self.indegrees[id] = 0
        self.vertexnum += 1

    def insert_edge(self, id1, id2):
        self.indegrees[id2] += 1
        self._outgoing[id1][id2] = Edge(self.coursetable[id1], self.coursetable[id2])
        self._incoming[id2][id1] = Edge(self.coursetable[id1], self.coursetable[id2])

    def all_pre_course_id(self, id):
        """return the set of id of pre courses"""
        l = set()
        for i in self._incoming[id].keys():
            l.add(i)
        return l

    def all_post_course_id(self, id):
        """return the set of id of post courses"""
        l = set()
        for i in self._outgoing[id].keys():
            l.add(i)
        return l

    def all_topology(self, id, path, indegrees_copy, min_found, max_course):
        """
        test all possible topology sorting ordering
        each time find a smaller term, print the arrangement in the screen
        """
        if len(path) == self.vertexnum:
            terms, arrangement = self.term_number(path, max_course, indegrees_copy)
            if terms < min_found[0]:
                min_found[0] = terms
                print(terms)
                del arrangement['virtual_root']
                print(arrangement)
        else:
            for i in self._outgoing[id].keys():
                self.indegrees[i] -= 1
            for i in self.vertices():
                if self.coursetable[i].state == 0 and self.indegrees[i] == 0:
                    self.coursetable[i].state = 2
                    tmp = [i for i in path]
                    path += [i]
                    self.all_topology(i, path, indegrees_copy, min_found, max_course)
                    path = tmp
                    self.coursetable[i].state = 0
            for i in self._outgoing[id].keys():
                self.indegrees[i] += 1

    def term_number(self, sequence, max_course, indegrees_copy):
        """
        Calculate the number of terms that are need for completing all the courses,
        given a legal topology sequence
        """
        terms = {}
        Q1 = my_queue()     # courses id to be selected in next term or later
        Q2 = my_queue()     # courses id to be selected in this term
        Q3 = my_queue()     # courses that have be studied, for recovering the "indegrees_copy" variable
        current_term = 0
        for i in sequence:
            Q1.in_queue(i)
        while not Q1.is_empty():
            for i in range(max_course):
                if Q1.is_empty():
                    break
                if indegrees_copy[Q1.get_head()] == 0:
                    course = Q1.out_queue()
                    terms[course] = current_term
                    Q2.in_queue(course)
                else:
                    break
            while not Q2.is_empty():
                course = Q2.out_queue()
                Q3.in_queue(course)
                for i in self._outgoing[course].keys():
                    indegrees_copy[i] -= 1
            current_term += 1
        while not Q3.is_empty():
            course = Q3.out_queue()
            for i in self._outgoing[course].keys():
                indegrees_copy[i] += 1
        return current_term - 1, terms

    def course_arrange(self, max_course):
        no_pre = []
        for i in self.vertices():
            if self.indegrees[i] == 0:
                no_pre.append(i)
        self.insert_vertex('virtual_root')
        for i in no_pre:
            self.insert_edge('virtual_root', i)
        self.coursetable['virtual_root'].state = 2
        indegrees_copy = copy.deepcopy(self.indegrees)
        self.all_topology('virtual_root', ['virtual_root'], indegrees_copy, [float('inf')], max_course)


if __name__ == "__main__":
    a = Graph()

    a.insert_vertex('A')
    a.insert_vertex('B')
    a.insert_vertex('C')
    a.insert_vertex('D')
    a.insert_vertex('E')
    a.insert_vertex('F')
    a.insert_vertex('G')
    a.insert_vertex('H')
    a.insert_vertex('I')
    a.insert_edge('A', 'B')
    a.insert_edge('A', 'C')
    a.insert_edge('B', 'D')
    a.insert_edge('B', 'E')
    a.insert_edge('B', 'F')
    a.insert_edge('C', 'G')
    a.insert_edge('D', 'E')
    a.insert_edge('D', 'H')
    a.insert_edge('E', 'F')
    a.insert_edge('E', 'G')
    a.insert_edge('F', 'G')
    a.insert_edge('G', 'H')
    a.insert_edge('H', 'I')

    a.course_arrange(6)
