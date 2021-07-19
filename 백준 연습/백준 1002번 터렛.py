import sys
for i in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = (abs(x1-x2)**2+abs(y1-y2)**2)**(1/2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif distance == r1+r2 or distance == abs(r1-r2):
        print(1)
    elif r1+r2 > distance > abs(r1 - r2):
        print(2)
    elif distance > r1+r2 or distance < abs(r1-r2):
        print(0)