import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    total_sum = [0] * (n+1)

    for i in range(n):
        if a_list[i] < b_list[i]:
            a_list[i] = b_list[i]

    for i in range(n-2,-1,-1) :
        if a_list[i] < a_list[i+1]:
            a_list[i] = a_list[i+1]

    for i in range(1, n+1):
        total_sum[i] += total_sum[i-1]
        total_sum[i] += a_list[i-1]

    for _ in range(q):
        qs, qe = map(int, input().split())
        print(total_sum[qe]-total_sum[qs-1],end=" ")
    print()