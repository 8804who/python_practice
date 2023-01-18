from itertools import combinations


def solution(relation):
    answer = 0
    student = {}
    key = {}
    lenColumn = len(relation[0])
    arr = [i + 1 for i in range(lenColumn)]
    for n in range(1, lenColumn + 1):
        for i in combinations(arr, n):
            student[i] = {}

    for s in relation:
        for n in range(1, lenColumn + 1):
            for i in combinations(arr, n):
                string = ''
                for j in i:
                    string += s[j - 1]
                if string in student[i]:
                    continue
                else:
                    student[i][string] = 1

    for n in range(1, lenColumn + 1):
        for i in combinations(arr, n):
            string = str(i).replace(',', '').replace('(', '').replace(')', '').replace(' ', '')
            unique = True
            for k in key:
                idx = 0
                keyLen = len(k)
                for s in k:
                    if s in string:
                        idx += 1
                if idx == keyLen:
                    unique = False
                    continue
            if unique and len(student[i]) == len(relation):
                key[string] = 1
                answer += 1
    return answer