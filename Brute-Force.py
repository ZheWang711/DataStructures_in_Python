__author__ = 'WangZhe'

class UVa725:

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

if __name__ == "__main__":
    sample = UVa725()
    sample.division(62)