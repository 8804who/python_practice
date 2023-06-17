import sys
n, m, k = map(int, sys.stdin.readline().split())

answer = 0
min_time = 1e9

for i in range(1, k+1):
    f, d = map(int, sys.stdin.readline().split())
    time = f*1+m-d
    if time<min_time:
        answer = i
        min_time=time
print(answer)