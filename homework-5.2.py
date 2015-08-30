__author__ = 'WangZhe'


class Data:
    __slots__ = 'key', 'value'

    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return str((self.key, self.value))

    def __hash__(self):
        # return hash((self.key, self.value))
        return hash(self.value)

    def __eq__(self, other):
        # return self.key == other.key and self.value == other.value
        return self.value == other.value

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key


class MinHeap:

    def __init__(self):
        self.map = {}   # A[map[data]] = data, mapping from Data object to index, for element deletion
        self.A = [None] # Heap main data structure
        self.time = 0   # time stamp, unique for every element

    def insert(self, key, value=None):
        '''
        :param key: the kay attribute in Heap element (Data)
        :param value: the value attribute in Heap element (Data)
        :return: None
        This function insert a new (key, value) Data element in the Heap in O(log n) time
        '''

        self.time += 1
        if value is None:
            value = self.time
        new_node = Data(key, value)
        self.A.append(new_node)
        self.map[new_node] = len(self.A) - 1
        tmp_pt = len(self.A) - 1
        ### bubble up ###
        while tmp_pt >= 2:
            if self.A[tmp_pt] < self.A[tmp_pt // 2]:
                self.map[self.A[tmp_pt]], self.map[self.A[tmp_pt // 2]] = self.map[self.A[tmp_pt // 2]], self.map[self.A[tmp_pt]]
                self.A[tmp_pt], self.A[tmp_pt // 2] = self.A[tmp_pt // 2], self.A[tmp_pt]
                tmp_pt //= 2
            else:
                break

    def min_son(self, index):
        '''
        Pre condition -- A[index] contains at least one son (2 * index <= len(A) - 1)
        Post condition -- exchange father and son node properly, return the index of the originally smaller son.
        :param index: the current father node that is going to be compared with its sons
        :return: new son index if the father is smaller, return None to terminate the loop in bubble_down
        '''
        tmp_pt = index
        two_son = True if 2 * tmp_pt + 1 <= len(self.A) - 1 else False
        if two_son:
            min_son = 2 * tmp_pt if self.A[2 * tmp_pt] < self.A[2 * tmp_pt + 1] else 2 * tmp_pt + 1
            if self.A[tmp_pt] > self.A[min_son]:
                        self.A[tmp_pt], self.A[min_son] = self.A[min_son], self.A[tmp_pt]
                        self.map[self.A[tmp_pt]], self.map[self.A[min_son]] = self.map[self.A[min_son]], self.map[self.A[tmp_pt]]
                        return min_son
            else:
                return None
        else:
            if self.A[tmp_pt] > self.A[2 * tmp_pt]:
                self.A[tmp_pt], self.A[2 * tmp_pt] = self.A[2 * tmp_pt], self.A[tmp_pt]
                self.map[self.A[tmp_pt]], self.map[self.A[2 * tmp_pt]] = self.map[self.A[2 * tmp_pt]], self.map[self.A[tmp_pt]]
                return 2 * tmp_pt
            else:
                return None

    def bubble_down(self, i):
        tmp_pt = i
        while 2 * tmp_pt <= len(self.A) - 1:
            tmp_pt = self.min_son(tmp_pt)
            if tmp_pt is None:
                break

    def extract_min(self):
        '''
        post condition: remove and return the element with smallest key in the Heap
        :return: The element with smallest key in the Heap
        '''
        tmp = self.A[1]
        self.A[1], self.A[-1] = self.A[-1], self.A[1]
        self.map[self.A[1]], self.map[self.A[-1]] = self.map[self.A[-1]], self.map[self.A[1]]
        del self.A[-1]
        del self.map[tmp]
        self.bubble_down(1)
        return tmp

    def remove(self, key, value):
        '''
        :param key: target key
        :param value: target value
        :return: target Data
        remove and return target Data in O(log n) time
        '''
        position = self.map[Data(key, value)]
        tmp = self.A[position]
        self.map[self.A[-1]], self.map[self.A[position]] = self.map[self.A[position]], self.map[self.A[-1]]
        self.A[-1], self.A[position] = self.A[position], self.A[-1]
        del self.map[self.A[-1]]
        del self.A[-1]
        self.bubble_down(position)
        return tmp


