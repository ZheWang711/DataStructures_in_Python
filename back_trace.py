__author__ = 'WangZhe'

class Queen:
    def __init__(self, n):
        x = [-1 for i in range(n)]
        S = {i for i in range(n)}
        self.result = self.Queen(n, S, x)

    # j is the col index
    def check(self, x, j, arranged_queen_num):
        for i in range(arranged_queen_num - 1):
            # i - arranged_queen_num + 1 = i - (arranged_queen_num - 1)
            # arranged_queen_hum - 1 is the row index of the newly inserted queen, whose column index is j
            tmp = (x[i] - j) / (i - arranged_queen_num + 1)
            if tmp == 1 or tmp == -1:
                return False
        return True

    def Queen(self, n, S, x):
        """
        :param n: total queen number
        :param S: unarranged Queen (column number, 0-based)
        :param x: the column index (0-based) for each queen on one row
        :return: self.result (number of solutions)
        """
        if len(S) == 0:
            print(x)
            return 1  # TODO: replace to the form of return value
            # return self.result
        else:
            result = 0
            for col in S:
                x[n - len(S)] = col
                S.remove(col)
                if self.check(x, col, n - len(S)):
                    result += self.Queen(n, S, x)
                S.add(col)
                x[n - len(S)] = -1
            return result


if __name__ == "__main__":
    print(Queen(8).result)

