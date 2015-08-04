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
        if current == len(A):
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




if __name__ == "__main__":
    sample = Permutation()
    A = [1, 1, 1, 2]
    sample.dictionary_order_print(A)
