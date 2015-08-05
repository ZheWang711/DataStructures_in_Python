__author__ = 'WangZhe'

def permutation(input_list):
    S = []
    A = []
    for i in range(len(input_list)):
        S.append(input_list[i])
        A.append(None)
    S.sort()
    _permutation(A, 0, S)

def _permutation(A, cur, S):
    if cur == len(A):
        print(A)
    else:
        for i in range(len(S)):
            if i == 0 or S[i] != S[i-1]:
                A[cur] = S[i]
                del S[i]
                _permutation(A, cur + 1, S)
                S.insert(i, A[cur])
                A[cur] = None

if __name__ =="__main__":
    permutation([1,3,1])