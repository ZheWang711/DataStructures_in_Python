__author__ = 'WangZhe'


class Queen:
    def __init__(self, n):
        self.x = x = [-1 for i in range(n)]
        self.S = S = {i for i in range(n)}
        self.result = self.Queen(n, S, x)
        self.find = self.QueenFind(n, S, x)

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

    def QueenFind(self, n, S, x):
        """
        :param n: total queen number
        :param S: unarranged Queen (column number, 0-based)
        :param x: the column index (0-based) for each queen on one row
        :return: self.result (number of solutions)
        """
        if len(S) == 0:
            print(x)
            return True
            # return self.result
        else:
            result = False
            for col in S:
                x[n - len(S)] = col
                S.remove(col)
                if self.check(x, col, n - len(S)):
                    if self.QueenFind(n, S, x):
                        result = True
                        S.add(col)
                        x[n - len(S)] = -1
                        break
                S.add(col)
                x[n - len(S)] = -1
            return result


import math
class TurnpikeReconstruction:
    def __init__(self, D):
        N = (1 + math.sqrt(1 + 8 * len(D))) / 2
        N = int(N)
        x = [-1 for i in range(N)]
        x[0] = 0
        self.solution = self.reconstruction(D, x, 1, N - 1)

    # delete the distances element in D if and only if the new assignment is legal
    def check_and_delete_upper_bound(self, D, x, l, u):
        tmp = []    # a copy of elements deleted from D, for recover use
        for i in x[0:l]:
            d = x[u] - i
            if d not in D:
                for elem in tmp:    # recover d if the operation failed
                    D.append(elem)
                return False
            else:
                tmp.append(d)
                D.remove(d)
        for i in x[u + 1:]:
            d = i - x[u]
            if d not in D:
                for elem in tmp:    # recover d if the operation failed
                    D.append(elem)
                return False
            else:
                tmp.append(d)
                D.remove(d)
        return True

    def check_and_delete_lower_bound(self, D, x, l, u):
        tmp = []    # a copy of elements deleted from D, for recover use
        for i in x[0:l]:
            d = x[l] - i
            if d not in D:
                for elem in tmp:    # recover d if the operation failed
                    D.append(elem)
                return False
            else:
                tmp.append(d)
                D.remove(d)
        for i in x[u + 1:]:
            d = i - x[l]
            if d not in D:
                for elem in tmp:    # recover d if the operation failed
                    D.append(elem)
                return False
            else:
                tmp.append(d)
                D.remove(d)
        return True


    def reconstruction(self, D, x, l, u):  # l and m are indexes of lower bound and upper bound to be assigned
        if l > u:
            print(x)
            return 1
        else:
            # choice 1
            solution = 0
            x[u] = max(D)
            if self.check_and_delete_upper_bound(D, x, l, u):
                solution += self.reconstruction(D, x, l, u - 1)
                # recover
                for i in x[0:l]:
                    d = x[u] - i
                    D.append(d)
                for i in x[u + 1:]:
                    d = i - x[u]
                    D.append(d)
            x[u] = -1

            # choice 2
            x[l] = x[len(x) - 1] - max(D)
            if self.check_and_delete_lower_bound(D, x, l, u):
                solution += self.reconstruction(D, x, l + 1, u)
                for i in x[0:l]:
                    d = x[l] - i
                    D.append(d)
                for i in x[u + 1:]:
                    d = i - x[l]
                    D.append(d)
            x[l] = -1
            return solution







if __name__ == "__main__":
    D = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 10]
    case1 = TurnpikeReconstruction(D)
    print(case1.solution)


