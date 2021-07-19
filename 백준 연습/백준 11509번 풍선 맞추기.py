import sys
n = int(sys.stdin.readline())
balloon = list(map(int, sys.stdin.readline().split()))
arrow = [0 for i in range(max(balloon))]
i = 0
count = 0
while i < n:
    if arrow[balloon[i]-1] == 0:
        if balloon[i] != 1:
            arrow[balloon[i]-2] += 1
        count += 1
    else:
        if balloon[i] == 1:
            arrow[0] -= 1
        else:
            arrow[balloon[i]-1] -= 1
            arrow[balloon[i]-2] += 1
    i += 1
print(count)