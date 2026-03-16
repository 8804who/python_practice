import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    p = [0]+list(map(int, input().split()))
    idx = 1

    while idx <= n and p[idx] == n - idx+1:
        idx += 1
    
    id = -1

    for i in range(idx, n+1):
        if p[i] == n - idx + 1:
            id = i
    
    for i in range(1, idx):
        print(p[i],end = ' ')
    
    if id != -1:
        for i in range(id, idx-1, -1):
            print(p[i],end = ' ')
        for i in range(id+1,n+1):
            print(p[i],end = ' ')
    print()