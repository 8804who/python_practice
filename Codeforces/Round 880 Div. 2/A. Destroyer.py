import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())

for test_case in range(t):
    n = int(input())
    l = list(map(int, input().rstrip().split()))

    d = defaultdict(int)

    answer = True

    for robot in l:
        if robot != 0:
            if d[robot-1] == 0:
                answer = False
                break
        d[robot] += 1

    if answer:
        print("YES")
    else:
        print("NO")