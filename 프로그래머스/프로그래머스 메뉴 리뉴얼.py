from itertools import combinations


def solution(orders, course):
    answer = []
    menu = {}

    menuComb = [[0] for _ in range(11)]
    maxCount = [0 for _ in range(11)]

    for i in orders:
        i = sorted(i)
        for j in course:
            for k in combinations(i, j):
                if "".join(k) in menu:
                    menu["".join(k)] += 1
                else:
                    menu["".join(k)] = 1

    for i in menu:
        if menu[i] > 1 and maxCount[len(i)] < menu[i]:
            maxCount[len(i)] = menu[i]
            menuComb[len(i)] = [i]
        elif 1 < menu[i] == maxCount[len(i)]:
            menuComb[len(i)].append(i)

    for i in course:
        if menuComb[i][0] != 0:
            for j in menuComb[i]:
                answer.append(j)
    answer.sort()
    return answer