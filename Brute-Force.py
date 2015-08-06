__author__ = 'WangZhe'
import math
import copy

class UVa725:
    """
    input integer n, to output all possible expressions
    in the form of abcde/fghij = n, where characters a to j
    corresponds with a complete permutation of 0 to 9 exactly
     ( There might be a precursor 0 in fghij, and 2 <= n <= 79 ).
    """

    def legal(self, a, b):
        buffer_string = str(a)
        a = [int(buffer_string[i]) for i in range(len(buffer_string))]
        buffer_string = str(b)
        b = [int(buffer_string[i]) for i in range(len(buffer_string))]
        if len(a) == 4:
            a.insert(0,0)
        set_a = set(a)
        set_b = set(b)
        if len(set_a) != 5 or len(set_b) != 5:
            return False
        for i in set_a:
            if i in set_b:
                return False
        return True

    def division(self, n):
        print(n)
        for i in range(1234, 98765 // n + 1):
            abcde = i
            fghij = n * i
            if self.legal(abcde, fghij):
                if abcde > 9999:
                    print("{0} / {1} = {2}".format(fghij, abcde, n))
                else:
                    print("{0} / 0{1} = {2}".format(fghij, abcde, n))


class Permutation:
    def dictionary_order_print(self, A):
        A = sorted(A)   # assign a new sequence, so that not to change the value of original sequence A
        self._dictionary_order_print(A, 0)

    def _dictionary_order_print(self, A, current):
        if current == len(A) - 1:
            print(A)
        else:
            for i in range(current, len(A)):
                # the for loop need to iterate over A's values non-repeatedly and non-omittedly
                # Thus recursive call if and only if A[i] is unequal with the element A[i - 1]
                # Since sequence A is already sorted, the index of same values in sequence A
                # must be distributed continuously
                if i == current or A[i] != A[i - 1]:
                    # the elements in the range of [0, current - 1] is fixed
                    # the first elements we need to consider about rearranging is at index [current]
                    tmp = A[i]
                    del(A[i])           # A.remove(tmp) this only remove the first element whose value is tmp
                    A.insert(current, tmp)  # current is the first position allowed to rearranging
                    self._dictionary_order_print(A, current + 1)
                    del(A[current])     # A.remove(tmp)
                    A.insert(i, tmp)


class SubsetGeneration:

    def _find(self, A, element):
        i = 0
        while i < len(A):
            if A[i] == element:
                return i
            i += 1
        raise ValueError("element {0} not found".format(element))

    def _increment_contruct(self, A, cur, B):
        # print("深度", cur)
        for i in range(cur):
            print(A[i], end=' ')
        print()

        low = 0 if not cur else self._find(B, A[cur - 1]) + 1
        for i in range(low, len(B)):
            A[cur] = B[i]
            self._increment_construct(A, cur + 1, B)
            A[cur] = None

    def increment_construct(self, B):
        A = [None for i in range(len(B))]
        self._increment_construct(A, 0, B)

    def bit_vector(self, A):
        V = [None for i in range(len(A))]
        self._bit_vector(A, V, 0)

    def _bit_vector(self, A, V, cur):
        if cur == len(V):
            for i in range(len(V)):
                if V[i] == 1:
                    print(A[i], end='')
            print()
        else:
            V[cur] = False
            self._bit_vector(A, V, cur + 1)
            V[cur] = True
            self._bit_vector(A, V, cur + 1)
            V[cur] = None


class PrimeRingProblem:
    def __init__(self, n):
        A = [i for i in range(2, n + 1)]
        V = [None for i in range(n)]
        V[0] = 1
        self.generate_ring(V, A, 1)

    def is_prime(self, n):
        for i in range(2, int(math.sqrt(n)) + 2):
            if n % i == 0:
                return False
        return True

    def generate_ring(self, V, A, cur):
        if cur == len(V) - 1:
            if self.is_prime(V[0] + A[0]) and self.is_prime(V[cur - 1] + A[0]):
                V[cur] = A[0]
                print(V)
                V[cur] = None
        else:
            for i in range(len(A)):
                if self.is_prime(A[i] + V[cur - 1]):
                    V[cur] = A[i]
                    del A[i]
                    self.generate_ring(V, A, cur + 1)
                    A.insert(i, V[cur])
                    V[cur] = None

class KryptonFactor:

    def __init__(self, L, k):
        import string
        self.D = {i: string.ascii_lowercase[i] for i in range(26)}
        self.count = 0
        self._KryptonFactor(L, k, 0, [])

    def _legal(self, A, elem):
        A.append(elem)
        for offset in range(1, len(A) // 2 + 1):
            flag = False     # assume exist, try to find one violation
            for i in range(offset):
                if A[len(A) - 1 - offset - i] != A[len(A) - 1 - i]:
                    flag = True     # not exist
            if not flag:    # if one exist, return, else continue finding
                del A[len(A) - 1]
                return False
        del A[len(A) - 1]
        return True

    def _KryptonFactor(self, L, k, cur, A):
        for i in range(L):
            if self._legal(A, self.D[i]):
                A.append(self.D[i])
                self.count += 1
                if self.count == k:
                    print(''.join(A))
                elif self.count < k:
                    # print(self.count, A)
                    self._KryptonFactor(L, k, cur + 1, A)
                del(A[len(A) - 1])

class Bandwidth:

    def __init__(self):
        self.Ver = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.Adj = {
            'A': ['F', 'B'],
            'B': ['G', 'C'],
            'D': ['G', 'C'],
            'F': ['A', 'G', 'H'],
            'E': ['H', 'D']
        }
        self.incoming = {
            'A': ['F'],
            'B': ['A'],
            'C': ['B', 'D'],
            'D': ['E'],
            'F': ['A'],
            'G': ['B', 'D', 'F'],
            'H': ['F', 'E']
        }
        self.found_min_result = float("inf")
        A = [None for i in range(len(self.Ver))]    # sequence generating
        B = {i: None for i in self.Ver}             # bandwidth
        I = {i: None for i in self.Ver}             # index A[i] = 'X' --> I['X'] = i
        n = len(self.Ver)
        self._bindwidth(n, 0, A, B, I)

    def _bindwidth(self, n, cur, A, B, I):
        if cur == n:
            tmp = max(B.values())
            if tmp < self.found_min_result:
                self.found_min_result = tmp
                print(tmp, ''.join(A))
                #print(B)

        else:
            for i in range(len(self.Ver)):
                #--------------------- cut -------------------------------------------------#
                if len(self.Adj.get(self.Ver[i], [])) >= self.found_min_result:
                    continue
                copy_B = copy.deepcopy(B)
                tmp = self.Ver[i]
                A[cur] = tmp
                I[tmp] = cur
                del self.Ver[i]
                #----------------------------- updating array B ----------------------------#
                for v in self.incoming.get(tmp, ''):
                    if v != '' and I[v] is not None:
                        B[v] = I[tmp] - I[v] if I[tmp] - I[v] > B[v] else B[v]
                #----------------------------- calculating B[A[cur]] -----------------------#
                max_node = 0
                for v in self.Adj.get(tmp, ''):
                    if v != '' and I[v] is not None:
                        max_node = I[tmp] - I[v] if I[tmp] - I[v] > max_node else max_node
                B[tmp] = max_node
                if max_node < self.found_min_result:
                    self._bindwidth(n, cur + 1, A, B, I)
                #----------------------------- recover global variable ---------------------#
                B = copy_B
                A[cur] = None
                self.Ver.insert(i, tmp)
                I[tmp] = None





if __name__ == "__main__":
    sample1 = Bandwidth()
