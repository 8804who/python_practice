import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    deposits = list(map(int, input().split()))

    total = 0
    answer = 0

    for i in range(n):
        total += deposits[i]//x 
        
    for i in range(n):
        answer = max(answer, deposits[i]+(total-deposits[i]//x)*y)
    print(answer)