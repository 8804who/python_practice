import sys
from collections import deque
array = deque([])
for i in range(int(sys.stdin.readline())):
    cmd = str(sys.stdin.readline())
    if cmd[0] == "p":
        if cmd[5] == "f":
            array.appendleft(cmd.split()[1])
        elif cmd[5] == "b":
            array.append(cmd.split()[1])
        elif cmd[5] == "r":
            print(array.popleft() if len(array)>0 else -1)
        else:
            print(array.pop() if len(array) > 0 else -1)
    else:
        if cmd[0]=="s":
            print(len(array))
        elif cmd[0]=="e":
            print(0 if len(array) > 0 else 1)
        elif cmd[0]=="f":
            print(array[0] if len(array) > 0 else -1)
        else:
            print(array[-1] if len(array) > 0 else -1)