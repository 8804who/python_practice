def reverse_coin(beginning, target):
    count = 0
    for i in range(len(beginning)):
        if beginning[i][0] != target[i][0]:
            count += 1
            for j in range(len(beginning[0])):
                beginning[i][j] += 1
                beginning[i][j] %= 2
    for j in range(len(beginning[0])):
        if beginning[0][j] != target[0][j]:
            count += 1
            for i in range(len(beginning)):
                beginning[i][j] += 1
                beginning[i][j] %= 2
    return count if beginning == target else -1


def solution(beginning, target):
    beginning2 = [[0 for _ in range(len(beginning[0]))] for _ in range(len(beginning))]
    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if j == 0:
                beginning2[i][j] = (beginning[i][j] + 1) % 2
            else:
                beginning2[i][j] = beginning[i][j]
    return min(reverse_coin(beginning, target), reverse_coin(beginning2, target) + 1)