"""
Missionaries and Cannibals -- a toy problem in Artificial Intelligence

In the missionaries and cannibals problem, three missionaries and three cannibals must cross a river using
a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries
present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries).
The boat cannot cross the river by itself with no people on board.

"""
__author__ = 'WangZhe'
import queue

class trans:
    def __init__(self, f, g, code):
        self.f = f  # number of missionaries in the boat
        self.g = g  # number of cannibals in the boat
        self.code = code    # for save memory in state.behav

    def __str__(self):
        return "{0}, {1}".format(self.f, self.g)


class state:
    def __init__(self, a, b, c, d, e, behav, n=0):
        self.a = a  # num of missionaries in left side
        self.b = b  # num of cannibals in left side
        self.c = c  # num of missionaries in right side
        self.d = d  # num of cannibals in right side
        self.e = e  # e = 0 if boat at left else 1
        self.n = n  # number of times of the boat crossing the river
        self.behav = behav  # memorizing the action chosen in each boat-crossing

    def __str__(self):
        return " state({0}, {1}, {2}, {3}, {4})".format(self.a, self.b, self.c, self.d, self.e)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d and self.e == other.e


# return None if illegal else return a new state
def carry_out(s, trans):
    if s.e == 0:
        a = s.a - trans.f
        b = s.b - trans.g
        c = s.c + trans.f
        d = s.d + trans.g
        e = 1
        behav = s.behav + [trans.code]
        if not ((a >= b >= 0 or a == 0 and b >= 0) and (c >= d >= 0 or c == 0 and d >= 0)):
            return None
    else:
        a = s.a + trans.f
        b = s.b + trans.g
        c = s.c - trans.f
        d = s.d - trans.g
        e = 0
        behav = s.behav + [trans.code]
        if not ((a >= b >= 0 or a == 0 and b >= 0) and (c >= d >= 0 or c == 0 and d >= 0)):
            return None
    new_s = state(a, b, c, d, e, behav, s.n + 1)
    return new_s

def generate_action(n):
    result = {}
    code = 0
    for i in range(1, n + 1):
        for j in range(0, i + 1):
            result[code] = trans(j, i - j, code)
            code += 1
    return result


def final(s, n):
    if s.a == 0 and s.b == 0 and s.c == n and s.d == n:
        return True
    return False

def list_find(l, item):
    for i in l:
        if i == item:
            return True
    return False


def planning(n=3):
    s = state(n, n, 0, 0, 0, [])
    actions = generate_action(2)
    Q = queue.Queue()
    L = []
    Q.put(s)
    L.append(s)

    while not Q.empty():
        s = Q.get()
        for action in actions.values():
            new_s = carry_out(s, action)
            if new_s is not None:
                if final(new_s, n):
                    return new_s.n, new_s.behav, actions
                else:
                    if not list_find(L, new_s):
                        L.append(new_s)
                        Q.put(new_s)
    return None, None, None


if __name__ == "__main__":
    n, behav, actions = planning(3)
    print(n, "steps")
    for i in behav:
        print(actions[i])
