__author__ = 'WangZhe'


class Node:
    __slots__ = 'key', 'x', 'element', 'left', 'right', 'father'

    def __init__(self, key, element):
        self.key = key
        self.element = element
        self.x = 1
        self.left = None
        self.right = None
        self.father = None

    def __eq__(self, other):
        return self.key == other.key

    def __le__(self, other):
        return self.key <= other.key

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __str__(self):
        father_key = self.father.key if self.father is not None else None
        return 'key: {0}, x: {1}, element: {2}, father key {3}'.format(self.key, self.x, self.element, father_key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        self.root = self._insert(self.root, new_node, None)

    def remove(self, node):
        self.root = self._remove(self.root, node)

    def _insert(self, root, new_node, father):
        if root is None:
            new_node.father = father
            return new_node
        elif new_node <= root:
            root.left = self._insert(root.left, new_node, root)
            root.x += 1
            return root
        else:
            root.right = self._insert(root.right, new_node, root)
            root.x += 1
            return root

    def _remove(self, root, node):  # delete the node with same key as para@node
        if root is None:
            raise ValueError('No element {0}'.format(node))
        elif node < root:
            root.left = self._remove(root.left, node)
            root.x -= 1
            return root
        elif node > root:
            root.right = self._remove(root.right, node)
            root.x -= 1
            return root
        else:   # node == root
            return self._delete_this_node(root)

    def _delete_this_node(self, root):
        if root.left is None and root.right is None:
            return None
        if root.left is None and root.right is not None:
            return root.right
        if root.right is None and root.left is not None:
            return root.left
        if root.left is not None and root.right is not None:
            tmp_pt = root.left
            while tmp_pt.right is not None:
                tmp_pt = tmp_pt.right
            tmp_pt.father.right = tmp_pt.left
            tmp_pt.left = root.left
            tmp_pt.right = root.right
            tmp_pt.left.father = tmp_pt
            tmp_pt.right.father = tmp_pt
            return tmp_pt

    def display(self, root, level):
        if root is not None:
            prefix = ''.join(['__|' for i in range(level)])
            print(prefix + str(root))
            self.display(root.left, level + 1)
            self.display(root.right, level + 1)


if __name__ == '__main__':
    T = BinarySearchTree()
    for i in [4, 1, 6, 3, 5, 7, 2]:
        T.insert(Node(i, str(i)))
    T.display(T.root, 1)
    T.remove(Node(3, 'b'))
    print()
    T.display(T.root, 1)
