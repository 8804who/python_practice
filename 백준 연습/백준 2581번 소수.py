import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
sum = 0
min = N
for i in range(M, N+1):
    j = 0
    for j in range(2, i+1):
        if i % j == 0:
            break
    if j == i:
        sum += j
        if j <= min:
            min = j
if sum > 0:
    print(sum)
    print(min)
else:
    print(-1)