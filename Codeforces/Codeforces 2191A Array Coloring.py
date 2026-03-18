import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    answer = "YES"
    colors = ['R'] * n

    for i in range(0,n,2):
        colors[nums[i]-1] = 'B'
    
    prev = ''
    for color in colors:
        if color == prev:
            answer = "NO"
        prev = color
    
    print(answer)