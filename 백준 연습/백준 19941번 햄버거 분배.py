import sys
N, K = map(int, sys.stdin.readline().split())
strInput = list(sys.stdin.readline().rstrip())
count = 0

if N < K:
    K = N

for i in range(N):
    if strInput[i] == "P":
        for j in range(-K, K+1):
            if 0 <= i+j < N:
                if strInput[i+j] == "H":
                    count += 1
                    strInput[i+j] = "N"
                    break

print(count, end="")