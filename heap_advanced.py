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
        # return 'key: {0}, x: {1}, element: {2}, father key {3}'.format(self.key, self.x, self.element, father_key)
        return 'key: {0}, element: {1}, father key {2}'.format(self.key, self.element, father_key)

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
            root.right.father = root.father
            return root.right
        if root.right is None and root.left is not None:
            root.left.father = root.father
            return root.left
        if root.left is not None and root.right is not None:
            tmp_pt = root.left
            while tmp_pt.right is not None:
                tmp_pt = tmp_pt.right
            if tmp_pt.father == root:
                tmp_pt.right = root.right
                tmp_pt.father = root.father
                root.right.father = tmp_pt
            else:
                if tmp_pt.left is not None:
                    tmp_pt.left.father = tmp_pt.father
                tmp_pt.father.right = tmp_pt.left
                tmp_pt.left = root.left
                tmp_pt.right = root.right
                root.left.father = tmp_pt
                root.right.father = tmp_pt
                tmp_pt.father = root.father
            return tmp_pt

    def search(self, target_key):
        return self._search(target_key, self.root)

    def _search(self, target_key, root):
        """target key must exist in the BST"""
        if target_key == root.key:
            return root
        elif target_key <= root.key and root.left is not None:
            return self._search(target_key, root.left)
        elif target_key > root.key and root.right is not None:
            return self._search(target_key, root.right)
        else:
            raise ValueError('target {0} not exist in BST'.format(target_key))

    def display(self, root, level):
        if root is not None:
            prefix = ''.join(['__|' for i in range(level)])
            print(prefix + str(root))
            self.display(root.left, level + 1)
            self.display(root.right, level + 1)

'''
class Element:
    __slots__ = 'element', 'id'

    def __init__(self, element):
        self.element = element
        self.id = hash(element)
'''


class Data:
    __slots__ = 'key', 'element', 'id'

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __init__(self, key, elem):
        self.key = key
        self.element = elem
        self.id = hash(elem)

    def __hash__(self):
        return hash(self.element)

    def __str__(self):
        return 'key: {0}; elem: {1}; identifier {2}'.format(self.key, self.element, self.id)


class Heap:
    # A = [Data] Data = Data(key, element, id)     id = hash(elem), key is the distance
    # BST Node = Node(key=A[i].id, element=i)

    def __init__(self):
        self.A = [None]
        self.BST = BinarySearchTree()

    def _bubble_up(self, index):
        father = index // 2
        while father >= 1 and self.A[father] > self.A[index]:
            father_id, index_id = self.A[father].id, self.A[index].id
            self.A[father], self.A[index] = self.A[index], self.A[father]
            self.BST.remove(Node(father_id, father))
            self.BST.remove(Node(index_id, index))
            self.BST.insert(Node(father_id, index))
            self.BST.insert(Node(index_id, father))
            index = father
            father //= 2

    def insert(self, key, elem):
        new_data = Data(key, elem)
        self.A.append(new_data)
        self.BST.insert(Node(new_data.id, len(self.A) - 1))
        self._bubble_up(len(self.A) - 1)

    def _bubble_down(self, index):
        while 2 * index + 1 <= len(self.A) - 1:    # 2 sons
            if self.A[2 * index] <= self.A[2 * index + 1]:
                father_id = self.A[index].id
                son_id = self.A[2 * index].id
                self.BST.remove(Node(father_id, index))
                self.BST.remove(Node(son_id, 2 * index))
                self.BST.insert(Node(father_id, 2 * index))
                self.BST.insert(Node(son_id, index))
                self.A[index], self.A[2 * index] = self.A[2 * index], self.A[index]
                index *= 2
            elif self.A[2 * index] > self.A[2 * index + 1]:
                father_id = self.A[index].id
                son_id = self.A[2 * index + 1].id
                self.BST.remove(Node(father_id, index))
                self.BST.remove(Node(son_id, 2 * index + 1))
                self.BST.insert(Node(father_id, 2 * index + 1))
                self.BST.insert(Node(son_id, index))
                self.A[index], self.A[2 * index + 1] = self.A[2 * index + 1], self.A[index]
                index = index * 2 + 1
        if 2 * index == len(self.A) - 1:
            father_id = self.A[index].id
            son_id = self.A[2 * index].id
            self.BST.remove(Node(father_id, index))
            self.BST.remove(Node(son_id, 2 * index))
            self.BST.insert(Node(father_id, 2 * index))
            self.BST.insert(Node(son_id, index))
            self.A[index], self.A[2 * index] = self.A[2 * index], self.A[index]

    def extract_min(self):
        id_1 = self.A[1].id
        id_last = self.A[-1].id
        self.BST.remove(Node(id_1, 1))
        self.BST.insert(Node(id_last, 1))
        self.BST.remove(Node(id_last, len(self.A) - 1))
        tmp = self.A[1]
        self.A[1] = self.A[-1]
        del self.A[-1]
        self._bubble_down(1)
        return tmp

    def remove(self, element):
        id = hash(element)
        pos = self.BST.search(id).element
        tmp = self.A[pos]
        id_pos = self.A[pos].id
        id_last = self.A[-1].id
        self.BST.remove(Node(id_pos, pos))
        self.BST.insert((Node(id_last, pos)))
        self.BST.remove(Node(id_last, len(self.A) - 1))
        self.A[pos] = self.A[-1]
        del self.A[-1]
        self._bubble_down(pos)
        return tmp

