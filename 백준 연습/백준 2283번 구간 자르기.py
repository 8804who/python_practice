import sys
N, K = map(int, sys.stdin.readline().split())

points = [0 for _ in range(1000001)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    points[s] += 1
    points[e] -= 1

for i in range(1, 1000000):
    points[i] += points[i-1]

s = 0
e = 0

total = points[0]
try:
    while True:
        if total > K:
            total -= points[s]
            s += 1
        elif total < K:
            e += 1
            total += points[e]
        else:
            print(str(s)+' '+str(e+1))
            break
except:
    print("0 0")
