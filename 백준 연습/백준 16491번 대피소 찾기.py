from itertools import permutations
import sys


def ccw(p1, p2,p3):
    cp = (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p3[0]*p2[1]+p2[0]*p1[1]+p1[0]*p3[1])
    if cp > 0:
        return 1
    elif cp == 0:
        return 0
    else:
        return -1


def check_cross(p1, p2, p3, p4):
    check1 = ccw(p1, p3, p4) * ccw(p2, p3, p4)
    check2 = ccw(p3, p1, p2) * ccw(p4, p1, p2)

    if check1 == 0 and check2 == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        if p3 <= p2 and p1 <= p4:
            return True
        else:
            return False
    elif check1 <= 0 and check2 <= 0:
        return True
    else:
        return False


N = int(sys.stdin.readline())
robots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shelters = [list(map(int, sys.stdin.readline().split()))+[i+1] for i in range(N)]

permutation_list = list(permutations(shelters, N))
for permutation in permutation_list:
    cross = False
    for idx in range(N):
        if cross:
            break
        robot1 = robots[idx]
        shelter1 = permutation[idx][:2]
        for check in range(idx+1, N):
            robot2 = robots[check]
            shelter2 = permutation[check][:2]
            if check_cross(robot1, shelter1, robot2, shelter2):
                cross = True
                break
    if not cross:
        for i in range(N):
            print(permutation[i][2])
        break
