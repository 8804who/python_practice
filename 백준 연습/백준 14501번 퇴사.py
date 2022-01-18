import sys
from collections import deque
N = int(sys.stdin.readline())
counseling = []
maxMoney = 0
for i in range(N):
    counseling.append(list(map(int, sys.stdin.readline().split())))
work = deque()
work.append([1, 0, 0])
while work:
    day, remain, money = work.popleft()
    if money > maxMoney:
        maxMoney = money
    if day <= N:
        if remain == 0:
            if day+counseling[day-1][0]-1 <= N:
                work.append([day+1, counseling[day-1][0]-1, money+counseling[day-1][1]])
            work.append([day+1, 0, money])
        else:
            work.append([day+1, remain-1, money])
print(maxMoney, end="")