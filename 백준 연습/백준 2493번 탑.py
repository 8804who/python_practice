import sys
from collections import deque
heightStack = deque()
numberStack = deque()
N = int(sys.stdin.readline())
towerList = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    while len(heightStack) > 0:
        if towerList[i] <= heightStack[-1]:
            print(numberStack[-1], end=" ")
            break
        else:
            heightStack.pop()
            numberStack.pop()
    if len(heightStack) == 0:
        print(0, end=" ")
    heightStack.append(towerList[i])
    numberStack.append(i+1)