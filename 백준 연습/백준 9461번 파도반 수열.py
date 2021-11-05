memo = [0 for i in range(101)]


def pado(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    elif n == 4:
        return 2
    elif n == 5:
        return 2
    else:
        if memo[n-1] == 0:
            p1 = pado(n-1)
            memo[n-1] = p1
        else:
            p1 = memo[n-1]
        if memo[n-5] == 0:
            p2 = pado(n-5)
            memo[n-5] = p2
        else:
            p2 = memo[n-5]
        return p1+p2


T = int(input())
for i in range(T):
    print(pado(int(input())))
