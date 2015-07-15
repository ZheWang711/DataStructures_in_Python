__author__ = 'WangZhe'
def test_exceptions():
    age = -1
    while age <= 0:
        try:
            age = int(input('input your age\n'))
            if age <= 0:
                print('your age must be positive')
        except(ValueError, EOFError):
            # print('invalid response')
            pass
    return


def sum_a(a, b, biteme = False):
    if biteme:
        print('biteme:', biteme)
    else:
        return a + b

def sum_b (a, b, *, biteme = False):
    if biteme:
        print('biteme', biteme)
    else:
        return a + b
a = [2]

def main():
    # a = 1
    test_namespace()

def test_namespace():
    a.append(1)
    print(a)