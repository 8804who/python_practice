import sys
from collections import deque
queue = deque([])
for i in range(int(sys.stdin.readline())):
    cmd = str(sys.stdin.readline()).split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif cmd[0] == "front":
        print(queue[0] if len(queue) != 0 else -1)
    else:
        print(queue[-1] if len(queue) != 0 else -1)