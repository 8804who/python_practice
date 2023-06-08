def ccw(p1, p2, p3):
    cp = (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p2[0]*p1[1]+p3[0]*p2[1]+p1[0]*p3[1])
    if cp > 0:
        return 1
    elif cp == 0:
        return 0
    else:
        return -1


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

con1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
con2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if con1 < 0 and con2 < 0:
    print(1)
else:
    print(0)