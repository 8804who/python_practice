import sys
N, M = map(int, sys.stdin.readline().split())
pw = {}
for i in range(N):
    site, password = sys.stdin.readline().split()
    pw[site] = password
for i in range(M):
    print(pw[sys.stdin.readline().strip()])
