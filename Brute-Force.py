__author__ = 'WangZhe'


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
                # the elements in the range of [0, current - 1] is fixed
                # the first elements we need to consider about rearranging is at index [current]
                tmp = A[i]
                A.remove(tmp)
                A.insert(current, tmp)  # current is the first position allowed to rearranging
                self._dictionary_order_print(A, current + 1)
                A.remove(tmp)
                A.insert(i, tmp)



if __name__ == "__main__":
    sample = Permutation()
    A = [1, 2, 3]
    sample.dictionary_order_print(A)
    print(A)