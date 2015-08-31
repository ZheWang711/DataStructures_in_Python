__author__ = 'WangZhe'


class bucket:

    def __init__(self):
        self.A = {}

    def insert(self, value):
        key = value // 10000
        if self.A.get(key) is None:
            self.A[key] = {value}
        else:
            self.A[key].add(value)

    def exist_key(self, key):
        return True if self.A.get(key) is not None else False




class Question1:

    def __init__(self):
        self.Solution()

    def Solution(self, filename='algo1-programming_prob-2sum.txt'):
        b = bucket()
        file = open(filename, 'r')
        for line in file:
            b.insert(int(line))
        print('result:', self.main(b))


    def main(self, bucket):
        result = set()
        for key in bucket.A.keys():
            for value_1 in bucket.A[key]:
                possible_keys = [i for i in [-key-2, -key-1, -key] if bucket.exist_key(i)]
                for key_2 in possible_keys:
                    for value_2 in bucket.A[key_2]:
                        tmp = value_1 + value_2
                        if -10000 <= tmp <= 10000 and value_1!= value_2:
                            result.add(tmp)
        return len(result)



'''
class Question1:

    def __init__(self):
        self.Solution()

    def main(self, array):
        array = sorted(array)
        result = 0
        for t in range(-10000, 10001):
            print(t)
            time1 = time.time()
            for i in array:
                if t - i != i and self.binary_search(array, 0, len(array)-1, t-i):
                    # print(t)
                    result += 1
                    break
            print(time.time() - time1)
        return result

    def Solution(self, filename='algo1-programming_prob-2sum.txt'):
        list = []
        file = open(filename, 'r')
        for line in file:
            list.append(int(line))
        # int_array = array.array('q', list)
        print(self.main(list))


    def binary_search(self, array, left, right, target):
        if left > right:
            return False
        if left == right:
            if array[left] == target:
                return True
            else:
                return False
        else:
            mid = left + (right - left + 1) // 2
            if array[mid] == target:
                return True
            else:
                if target < array[mid]:
                    return self.binary_search(array, left, mid - 1, target)
                if target > array[mid]:
                    return self.binary_search(array, mid + 1, right, target)




def binary_search(array, left, right, target):
        if left > right:
            return False
        if left == right:
            if array[left] == target:
                return True
            else:
                return False
        else:
            mid = left + (right - left + 1) // 2
            if array[mid] == target:
                return True
            else:
                if target < array[mid]:
                    return binary_search(array, left, mid - 1, target)
                if target > array[mid]:
                    return binary_search(array, mid + 1, right, target)

'''
if __name__ == '__main__':
    Question1()