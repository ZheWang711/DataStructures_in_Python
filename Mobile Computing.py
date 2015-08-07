__author__ = 'WangZhe'
"""
reference: https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=4100
testing case from: http://blog.csdn.net/kun768/article/details/43272449
"""

def _is_equal(self, other):
        if self is None and other is None:
            return True
        if self is not None and other is None:
            return False
        if self.weight != other.weight:
            return False
        if _is_equal(self.left_son, other.left_son) and _is_equal(self.right_son, other.right_son):
            return True


def balance(self):
    """
    ONLY called from ROOT!
    construct --> insertnode --> balance
    """
    if not self.is_leaf:
        self.left_son.hang_point = (self.hang_point * self.weight - self.right_son.weight) / self.weight
        self.right_son.hang_point = 1 + self.left_son.hang_point
        balance(self.left_son)
        balance(self.right_son)


def get_max(root):
    if root.is_leaf:
        return root.hang_point
    else:
        return max(get_max(root.left_son), get_max(root.right_son))


def get_min(root):
    if root.is_leaf:
        return root.hang_point
    else:
        return min(get_min(root.left_son), get_min(root.right_son))


def get_length(root):
    return get_max(root) - get_min(root)


class TreeNode:
    def __init__(self, x=0, w=0, is_leaf=True, left=None, right=None):
        self.is_leaf = is_leaf
        self.hang_point = x         # unavailable until balanced
        self.weight = w
        self.left_son = left
        self.right_son = right

    def insert_left(self, left_son):
        self.weight += left_son.weight
        self.left_son = left_son
        self.is_leaf = False

    def insert_right(self, right_son):
        self.weight += right_son.weight
        self.right_son = right_son
        self.is_leaf = False

    def __str__(self):
        return str(self.weight)

    def __eq__(self, other):
        return _is_equal(self, other)


class MobileComputing:
    def __init__(self, limit, weight_array):
        self.limit = limit # global ---------------------------------
        self.found_max_allowed = -float('inf') # global -----------------
        self.result = []
        A = [TreeNode(w=i) for i in weight_array]
        cur = 0
        # root = None
        n = len(weight_array)
        self.mobile_computing(cur, A, n)
        print(self.result[-1]) if len(self.result) != 0 else print("None")

    def mobile_computing(self, cur, A, n):
        if cur == n - 1:
            length = get_length(A[0])
            #print(length)
            if self.found_max_allowed < length <= self.limit:
                self.found_max_allowed = length
                self.result.append(length)
        else:
            for i in range(len(A)):
                for j in range(len(A)):
                    if i != j:
                        new_node = TreeNode()
                        new_node.insert_left(A[i])
                        new_node.insert_right(A[j])
                        balance(new_node)
                        if get_length(new_node) > self.limit:
                            continue

                        if j > i:
                            del A[j]
                            del A[i]
                            A.append(new_node)
                            self.mobile_computing(cur + 1, A, n)
                            del A[len(A) - 1]
                            A.insert(i, new_node.left_son)
                            A.insert(j, new_node.right_son)
                        if i > j:
                            del A[i]
                            del A[j]
                            A.append(new_node)
                            self.mobile_computing(cur + 1, A, n)
                            del A[len(A) - 1]
                            A.insert(j, new_node.right_son)
                            A.insert(i, new_node.left_son)


if __name__ == "__main__":
    # MobileComputing(1.3, [3, 1, 2, 1])
    # MobileComputing(1.4, [3, 1, 2, 1])
    # MobileComputing(2.0, [3, 1, 2, 1])
    MobileComputing(1.59, [4, 2, 1, 1, 3])
    MobileComputing(1.7143, [4, 1, 2, 3, 5])



"""
for manually debug
    a = TreeNode(w=1)
    b = TreeNode(w=1)
    c = TreeNode(w=2)
    d = TreeNode(w=3)
    e = TreeNode()
    e.insert_left(d)
    e.insert_right(b)
    f = TreeNode()
    f.insert_left(e)
    f.insert_right(c)
    g = TreeNode()
    g.insert_left(a)
    g.insert_right(f)
    balance(g)
    print(get_length(g))
"""


