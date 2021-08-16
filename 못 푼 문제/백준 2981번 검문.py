import sys

n = int(sys.stdin.readline())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
m.sort()
divisor = []
for i in range(2, m[0]+1):
    div = True
    for j in divisor:
        if i % j == 0:
            div = False
            break
    if div:
        remain = m[0] % i
        for k in m:
            print("i는", i, "k는", k, "나머지는", k % i)
            if k % i != remain:
                divisor.append(i)
                break
            if k == m[-1]:
                print(i)
