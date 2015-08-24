__author__ = 'WangZhe'


class Data:
    def __hash__(self):
        return hash((self.key, self.value))

    def __init__(self, k, value):
        self.key = k
        self.value = value

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __str__(self):
        return 'key {0}, value {1}'.format(self.key, self.value)


class Heap:
    def __init__(self):
        self.A = [None]
        self.time = 0
        self.map = {}  # obj --> time
        self.pos = [None]  # time --> position

    def _bubble_up(self, i):
        if i // 2 >= 1 and self.A[i // 2].key > self.A[i].key:
            self.A[i // 2], self.A[i] = self.A[i], self.A[i // 2]
            self.pos[self.map[self.A[i // 2]]], self.pos[self.map[self.A[i]]] = self.pos[self.map[self.A[i]]], \
                                                                                self.pos[self.map[self.A[i // 2]]]
            return self._bubble_up(i // 2)
        else:
            return i

    def _bubble_down(self, i):
        if 2 * i + 1 <= len(self.A) - 1:  # have 2 son
            if self.A[2 * i].key < self.A[2 * i + 1].key and self.A[i].key > self.A[2 * i].key:
                self.A[i], self.A[2 * i] = self.A[2 * i], self.A[i]
                self.pos[self.map[self.A[2 * i]]], self.pos[self.map[self.A[i]]] = self.pos[self.map[self.A[i]]], \
                                                                                    self.pos[self.map[self.A[2 * i]]]

                self._bubble_down(2 * i)
            if self.A[2 * i + 1].key < self.A[2 * i].key and self.A[i].key > self.A[2 * i + 1].key:
                self.A[i], self.A[2 * i + 1] = self.A[2 * i + 1], self.A[i]
                self.pos[self.map[self.A[2 * i + 1]]], self.pos[self.map[self.A[i]]] = self.pos[self.map[self.A[i]]], \
                                                                                self.pos[self.map[self.A[2 * i + 1]]]
                self._bubble_down(2 * i + 1)
        elif 2 * i == len(self.A) - 1 and self.A[i].key > self.A[2 * i].key:  # have 1 son
            self.A[i], self.A[2 * i] = self.A[2 * i], self.A[i]
            self.pos[self.map[self.A[2 * i]]], self.pos[self.map[self.A[i]]] = self.pos[self.map[self.A[i]]], \
                                                                                   self.pos[self.map[self.A[2 * i]]]

    def insert(self, obj):  # obj has a key attribute
        self.A.append(obj)
        self.time += 1
        self.map[obj] = self.time
        self.pos.append(self.time)
        self._bubble_up(len(self.A) - 1)

    def extract_min(self):
        tmp = self.A[1]
        self.A[1] = self.A[len(self.A) - 1]
        del self.A[len(self.A) - 1]

        self.pos[self.map[tmp]] = None
        del self.map[tmp]
        self.pos[self.map[self.A[1]]] = 1

        self._bubble_down(1)

    def remove_obj(self, obj):
        time_stamp = self.map[obj]
        position = self.pos[time_stamp]

        tmp = self.A[position]
        self.A[position] = self.A[len(self.A) - 1]
        del self.A[len(self.A) - 1]
        self.pos[self.map[tmp]] = None
        del self.map[tmp]
        self.pos[self.map[self.A[position]]] = position

        self._bubble_down(position)




if __name__ == '__main__':
    H = Heap()
    for i in range(10):
        H.insert(Data(i, str(i)))
    print(H.insert(Data(2, 'A')))
    H.remove_obj(Data(1, '1'))
    a = 1
