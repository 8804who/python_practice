import sys

input = sys.stdin.readline

t= int(input())

for _ in range(t):
    s, k ,m = map(int, input().split())

    if m//k % 2 == 1:
        s = min(s,k)
    
    print(max(0, s-m%k))