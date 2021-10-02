import sys


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


n = int(sys.stdin.readline())
m = []
remain = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
m.sort()
print(gcd(gcd(m[0], m[1]), gcd(m[-2], m[-1])))