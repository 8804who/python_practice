import sys
N, K = map(int, sys.stdin.readline().split())
strInput = list(sys.stdin.readline().rstrip())
strInput2 = []
for i in range(N):
    strInput2.append(strInput[i])
count = 0
count2 = 0
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
            elif i+j < N:
                break

for i in range(N-1, -1, -1):
    if strInput2[i] == "P":
        for j in range(K, -K-1, -1):
            if 0 <= i+j < N:
                if strInput2[i+j] == "H":
                    count2 += 1
                    strInput2[i+j] = "N"
                    break
            elif i+j < 0:
                break

print(max(count, count2), end="")