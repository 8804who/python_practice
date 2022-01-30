import sys
A, B = map(int, sys.stdin.readline().split())
A, B = max(A, B), min(A,B)
while True:
    r = A % B
    if r > 0:
        A, B = B, r
    else:
        break
for i in range(B):
    print(1, end="")