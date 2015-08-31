__author__ = 'WangZhe'
'''
reference: http://bbs.csdn.net/topics/390705054
'''

class Solution:
    def __init__(self):
        self.people = [i for i in range(99, 75, -1)]
        self.table = {i: [] for i in range(3)}
        self.sum = [0 for i in range(3)]
        self.average_table = sum(self.people) // 3
        self.cnt = 0
        print(self.divide_table(0, -1))

    def divide_table(self, finished_number, max_assigned):
        for i in range(3):
            if len(self.table[i]) == len(self.people) // 3 and self.sum[i] != self.average_table:
                return 0

        if finished_number == len(self.people):
            for i in range(3):
                if self.sum[i] != self.average_table:
                    raise ValueError('unevenly finished')
            self.cnt += 1
            if self.cnt % 10 == 0:
                print(self.cnt)
            return 1
        else:
            result = 0
            person = self.people[finished_number]
            for i in range(0, min(max_assigned + 2, 3)):
                if self.sum[i] + person <= self.average_table and len(self.table[i]) < len(self.people) // 3:
                    self.sum[i] += person
                    self.table[i].append(person)
                    result += self.divide_table(finished_number + 1, max(max_assigned, i))
                    del self.table[i][-1]
                    self.sum[i] -= person
            return result


if __name__ == '__main__':
    Solution()


