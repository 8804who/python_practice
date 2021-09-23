import sys

n = int(sys.stdin.readline())
m = []
remain = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
m.sort()
for i in range(1, len(m)+1):
    remain[i] = m[i] % m[0]
gfc = 1
for i in range(len(remain)):
    if remain[i] % gfc !=0:
        gfc=