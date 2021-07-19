import sys
M, N = map(int, sys.stdin.readline().split())
prime = [False, False]+[True]*(N-1)
for i in range(2, N):
    if prime[i]:
        j = 2
        while i*j <= N:
            prime[i*j] = False
            j += 1
for i in range(M, N+1):
    if prime[i]:
        print(i)