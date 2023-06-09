def CCW(p1, p2, p3):
    cp = (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p3[0]*p2[1]+p2[0]*p1[1]+p1[0]*p3[1])
    if cp > 0:
        return 1
    elif cp == 0:
        return 0
    else:
        return -1


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

ccw1 = CCW(p1, p3, p4) * CCW(p2, p3, p4)
ccw2 = CCW(p3, p1, p2) * CCW(p4, p1, p2)

if ccw1 == 0 and ccw2 == 0:
    if p1>p2:
        p1, p2 = p2, p1
    if p3>p4:
        p3, p4 = p4, p3
    if p3 <= p2 and p1 <= p4:
        print(1)
    else:
        print(0)
elif ccw1 <= 0 and ccw2 <= 0:
    print(1)
else:
    print(0)