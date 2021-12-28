from collections import deque
import sys

N = int(sys.stdin.readline())
n = deque()
arr = list(map(int, sys.stdin.readline().split()))
for i in range(1, N+1):
    n.append(i)

count = 0
while True:
    if len(n) == N:
        output = n.popleft()
    else:
        if arr[output-1] > 0:
            output = n.popleft()
        else:
            output = n.pop()

    if len(n) == 0:
        break
    print(output, end=" ")

    if arr[output-1] > 0:
        while count < arr[output-1]-1:
            count += 1
            n.append(n.popleft())
    else:
        while count > arr[output-1]+1:
            count -= 1
            n.appendleft(n.pop())
    count = 0
print(output, end="")