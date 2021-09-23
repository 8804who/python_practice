import sys
for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline()
    n = int(sys.stdin.readline())
    input = sys.stdin.readline()
    arr = list(map(int, input[1:-2].split(sep=",")) if n != 0 else [])
    order = cmd[0:-1].split("R")
    if n < len(cmd)-len(order):
        print("error")
    elif n == len(cmd)-len(order):
        print("[]")
    else:
        front_del = 0
        for j in range(len(order)):
            if j % 2 == 1:
                del arr[len(arr)-order[j].count("D"):]
            else:
                front_del += order[j].count("D")
        print("[", end="")
        if len(order) % 2 == 1:
            for j in range(front_del, len(arr)):
                print(arr[j], ",", sep="", end="") if j != len(arr)-1 else print(arr[j], end="")
        else:
            for j in range(len(arr)-1, front_del-1, -1):
                print(arr[j], ",", sep="", end="") if j != front_del else print(arr[j], end="")
        print("]")