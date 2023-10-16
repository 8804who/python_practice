import sys
N = int(sys.stdin.readline())
lock = list(map(int, sys.stdin.readline().split()))

solved = False

for second in range(1, N):
    lock.insert(0, lock[-1])
    lock.pop(-1)
    s = -1
    e = -1
    for idx in range(N-1):
        if lock[idx+1] == lock[idx]-1 or (lock[idx] != 9 and lock[idx+1] == 10):
            if s == -1:
                s = idx
            e = idx+1
    temp = lock[:s]+list(reversed(lock[s:e+1]))+lock[e+1:]
    for first in range(1, N):
        temp.insert(0, temp[-1])
        temp.pop(-1)
        for i in range(1, N + 1):
            if temp[i - 1] != i:
                break
            if i == N:
                print(first)
                print(s + 1, e + 1)
                print(second)
                solved = True
                break
    if solved:
        break