from collections import deque
queue = deque()
A, B = map(int, input().split())
arr = dict()
queue.append(A)
arr[A] = 1
while len(queue) > 0:
    num = queue.popleft()
    if num*2 <= B:
        if num*2 not in arr:
            arr[num*2] = arr[num]+1
            queue.append(num*2)
    if int(str(num)+'1') <= B:
        if int(str(num)+'1') not in arr:
            arr[int(str(num)+'1')] = arr[num]+1
            queue.append(int(str(num)+'1'))
if B in arr:
    print(arr[B], end="")
else:
    print(-1, end="")