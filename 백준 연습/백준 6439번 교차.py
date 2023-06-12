def CCW(p1, p2, p3):
    cp = (p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1])-(p3[0]*p2[1]+p2[0]*p1[1]+p1[0]*p3[1])
    if cp > 0:
        return 1
    elif cp == 0:
        return 0
    else:
        return -1


def check_cross(p1, p2, p3, p4):
    ccw1 = CCW(p1, p3, p4) * CCW(p2, p3, p4)
    ccw2 = CCW(p3, p1, p2) * CCW(p4, p1, p2)

    if ccw1 == 0 and ccw2 == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        if p3 <= p2 and p1 <= p4:
            return True
        else:
            return False
    elif ccw1 <= 0 and ccw2 <= 0:
        return True
    else:
        return False


T = int(input())

for test_case in range(T):
    lx1, ly1, lx2, ly2, bx1, by1, bx2, by2 = map(int, input().split())

    if bx1 > bx2:
        bx1, bx2 = bx2, bx1

    if by1 > by2:
        by1, by2 = by2, by1

    if bx1 < lx1 < bx2 and bx1 < lx2 < bx2 and by1 < ly1 < by2 and by1 < ly2 < by2:
        print("T")
        continue

    l1, l2 = (lx1, ly1), (lx2, ly2)

    b1, b2, b3, b4 = (bx1, by1), (bx1, by2), (bx2, by1), (bx2, by2)

    if check_cross(l1, l2, b1, b2) or check_cross(l1, l2, b1, b3) or check_cross(l1, l2, b2, b4) or check_cross(l1, l2, b3, b4):
        print("T")
    else:
        print("F")