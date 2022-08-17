import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

palindrome = [[0 for _ in range(N + 1)] for _ in range(N + 1)]


print(palindrome)
M = int(sys.stdin.readline())
for i in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(palindrome[S][E])