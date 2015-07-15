__author__ = 'WangZhe'

#----------------------- P-1.29 --------------------#


def all_possible_strings(fixed, characters, fixed_characters):
    combination_number = 0
    n = len(characters)
    if fixed == n:
        print(' '.join(fixed_characters))
        return 1
    else:
        for i in range(n):
            if characters[i][1] == 0:  # unfixed
                characters[i][1] = 1
                fixed_characters.append(characters[i][0])
                combination_number += all_possible_strings(fixed + 1, characters, fixed_characters)
                del fixed_characters[-1]
                characters[i][1] = 0
        return combination_number

if __name__ == '__main__':
    characters = [['c', 0], ['a', 0], ['t', 0], ['d', 0], ['o', 0], ['g', 0]]  # char[i][1] == 0 unfixed
    # characters = [['a', 0], ['b', 0], ['c', 0], ['d', 0]]
    n = all_possible_strings(0, characters, [])
    print(n)











