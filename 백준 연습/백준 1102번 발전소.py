from collections import deque
import sys
N = int(sys.stdin.readline())

costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

usable = sys.stdin.readline().rstrip()
facility = 0

for i, YN in enumerate(usable):
    if YN == 'Y':
        facility += 1 << (N-1-i)

usable = str(bin(facility)).count('1')
P = int(sys.stdin.readline())

if usable >= P:
    print('0')
elif usable == 0:
    print('-1')
else:
    dp = [1e9 for _ in range(1 << N)]
    q = deque()
    q.append([facility, usable, 0])
    answer = 1e10
    while q:
        f, u, price = q.pop()
        if u == P:
            if answer > price:
                answer = price
            continue
        for i in range(N):
            if not f & (1 << (N-1-i)):
                cost = 1e9
                for j in range(N):
                    if f & (1 << (N-1-j)) and costs[j][i] < cost:
                        cost = costs[j][i]
                if price+cost < dp[f | (1 << (N-1-i))]:
                    q.append([f | (1 << (N-1-i)), u+1, price+cost])
                    dp[f | (1 << (N-1-i))] = price+cost
    print(answer)
