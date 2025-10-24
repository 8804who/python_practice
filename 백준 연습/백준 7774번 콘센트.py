import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

A_concent = 1
B_concent = 0

while A and B:
    while A_concent>0 and A:
        if B_concent >= len(B):
            break
        B_concent += A[0]
        A_concent -= 1
        A.pop(0)

    while B_concent>0 and B:
        A_concent += B[0]
        B_concent -= 1
        B.pop(0)
print(A_concent)