from itertools import product
import bisect
import sys

n = int(sys.stdin.readline())

answer = 0
A, B, C, D = [], [], [], []

for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
CD = []

for i in product(A, B):
    AB.append(i[0]+i[1])
for i in product(C, D):
    CD.append(i[0]+i[1])

AB.sort()
CD.sort()
len_AB = len(AB)

AB_idx = 0
CD_idx = len(CD)-1


while AB_idx < len_AB and CD_idx >= 0:
    num1 = AB[AB_idx]
    num2 = CD[CD_idx]

    if num1+num2 > 0:
        CD_idx -= 1
    elif num1+num2 == 0:
        AB_next = bisect.bisect_right(AB, num1)
        CD_next = bisect.bisect_left(CD, num2) - 1
        answer += (AB_next - AB_idx) * (CD_idx - CD_next)
        AB_idx = AB_next
        CD_idx = CD_next
    else:
        AB_idx += 1
print(answer)