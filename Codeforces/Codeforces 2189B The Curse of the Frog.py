import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    max_dist = 0

    for _ in range(n):
        a, b, c = map(int, input().split())
        x -= a*(b-1)
        max_dist = max(max_dist, a*b-c)

    if x <= 0:
        print(0)
    elif max_dist == 0:
        print(-1)
    else:
        print((x+max_dist-1)//max_dist)
