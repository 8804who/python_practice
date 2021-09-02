t = int(input())
for i in range(t):
    s = list(input())
    t1, t2 = 0, 0
    c1, c2 = 5, 5
    q1, q2 = 0, 0
    for j in range(10):
        if j % 2 == 0:
            if s[j] == "1":
                t1 += 1
            if s[j] == "?":
                q1 += 1
            c1 -= 1
        else:
            if s[j] == "1":
                t2 += 1
            if s[j] == "?":
                q2 += 1
            c2 -= 1
        if j >= 5:
            if (t1 + q1) - t2 > c2:
                break
            elif (t2 + q2) - t1 > c1:
                break
    print(j + 1)
