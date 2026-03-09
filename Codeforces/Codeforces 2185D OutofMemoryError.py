import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())

    arr1, arr2 = [0],[0]
    stack = []

    for num in list(map(int, input().split())):
        arr1.append(num)
        arr2.append(num)

    for _ in range(m):
        b, c = map(int, input().split())
        stack.append(b)
        arr2[b] += c
        if arr2[b] > h:
            while stack:
                idx = stack.pop()
                arr2[idx] = arr1[idx]
    
    print(*arr2[1:])