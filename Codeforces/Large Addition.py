import sys

t = int(sys.stdin.readline())

for testcase in range(t):
    x = int(sys.stdin.readline())
    while x > 0:
        if x % 10 < 9:
            x -= 10
        else:
            break
        x //= 10

    if x == 0:
        print("YES")
    else:
        print("NO")