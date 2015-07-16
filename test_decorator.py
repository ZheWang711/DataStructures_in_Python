__author__ = 'WangZhe'

# -------------- closures ------------------ #
def outer(x):
    # x = 1
    def inner():
        def innner():
            print(x)
        return innner
    return inner

def my_filter(function, list):
    return [x for x in list if function(x)]

# def list_sort(index, l):
  #   retrive = [l[i][index] for i in l]
    # def

def check_closures():
    l = [[i, -i] for i in range(10)]
    # print(my_filter(lambda x: x % 2 == 0, l))
    print(sorted(l, key=lambda x: x[0]))

# --------------- decorator ----------------- #
# reference: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# A decorator practice which add a boundary checker for add() and sub() functions


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


def add(x, y):
    return Coordinate(x.x + y.x, x.y + y.y)


def sub(x, y):
    return Coordinate(x.x - y.x, x.y - y.y)


def limit_bound(x):
    return x if x > 0 else 0


# a decorator for checking lower bound (lower bound >= 0)
def boundary_check(func):
    def checker(x, y):
        x = Coordinate(limit_bound(x.x), limit_bound(x.y))
        y = Coordinate(limit_bound(y.x), limit_bound(y.y))
        result = func(x, y)
        return Coordinate(limit_bound(result.x), limit_bound(result.y))
    return checker


def test_decorator(add, sub):
    add = boundary_check(add)
    sub = boundary_check(sub)
    p1 = Coordinate(100, 200)
    p2 = Coordinate(300, 200)
    p3 = Coordinate(-100, -100)
    print(sub(p1, p2))
    print(add(p1, p3))

if __name__ == "__main__":
    test_decorator(add, sub)

