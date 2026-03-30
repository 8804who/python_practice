import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    seats = list(input().rstrip())

    if n == 1:
        seats[0] = '1'

    if 2 <= n:
        if seats[0] == '0':
            seats[1] = '1'

        for i in range(2, n):
            if seats[i-2] == '0' and seats[i-1] == '0':
                seats[i] = '1'
        
        if seats[-2] == '0':
            seats[-1] = '1'
    print(seats.count('1'))
