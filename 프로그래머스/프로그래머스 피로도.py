from itertools import permutations


def solution(k, dungeons):
    answer = -1
    lenDungeon = len(dungeons)
    arr = [i for i in range(lenDungeon)]

    for i in permutations(arr, lenDungeon):
        explored = 0
        point = k
        for j in i:
            if point >= dungeons[j][0]:
                point -= dungeons[j][1]
                explored += 1
        if answer < explored:
            answer = explored
    return answer