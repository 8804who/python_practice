import sys


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


n = int(sys.stdin.readline())
m = []
diff = []
result = []
for i in range(n):
    m.append(int(sys.stdin.readline()))

m.sort()

for i in range(1, n):
    diff.append(m[i]-m[i-1])

prev = diff[0]
for i in range(1, n-1):
    prev = gcd(prev, diff[i])

for i in range(2, int(prev**(1/2))+1):
    if prev % i == 0:
        result.append(i)

length = len(result)
for i in range(length-1, -1, -1):
    if prev / result[i] != result[i]:
        result.append(int(prev/result[i]))
result.append(prev)

for i in range(len(result)):
    print(result[i], end=" ")