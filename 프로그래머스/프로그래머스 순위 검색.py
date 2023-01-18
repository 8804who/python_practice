from itertools import combinations
from bisect import bisect_left


def solution(infos, query):
    answer = []
    d = {}
    for info in infos:
        s = info.split(' ')
        for i in range(5):
            for c in combinations(s[0:4], i):
                string = str(c).replace('(', '').replace(')', '')
                string = string.replace('\'', '').replace(',', '')
                string = string.replace(' ', '')
                if string in d:
                    d[string].append(int(s[4]))
                else:
                    d[string] = [int(s[4])]

    for i in d:
        d[i].sort()

    for i in range(len(query)):
        query[i] = query[i].replace('and', '').replace('  ', ' ')
        que = query[i].split(' ')
        string = ''
        p = 0
        for q in que[0:4]:
            if q != '-':
                string += q
        if string not in d:
            answer.append(0)
        else:
            idx = bisect_left(d[string], int(que[4]))
            answer.append(len(d[string]) - idx)
    return answer