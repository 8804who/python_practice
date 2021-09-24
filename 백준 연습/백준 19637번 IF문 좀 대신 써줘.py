import sys

N, M = map(int, sys.stdin.readline().split())
title = []
for i in range(N):
    title.append(sys.stdin.readline().split())
for i in range(M):
    n = int(sys.stdin.readline())
    first = 0
    last = N-1
    while True:
        pivot = int((first+last)/2)
        if first >= last:
            print(title[pivot][0])
            break
        if n > int(title[pivot][1]):
            first = pivot+1
        else:
            last = pivot

