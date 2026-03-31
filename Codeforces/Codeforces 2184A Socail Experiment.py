import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    if n < 4:
        print(n)
    else:
        print(n%2)