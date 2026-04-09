import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    requrirements = []

    for _ in range(n):
        a, b = map(int, input().split())
        requrirements.append((a, b))
    
    answer = 0
    position = 0
    time = 0
    for i in range(n):
        answer += requrirements[i][0]-time
        if requrirements[i][1] == position and (requrirements[i][0]-time)%2==1:
            answer -= 1
        elif requrirements[i][1] != position and (requrirements[i][0]-time)%2==0:
            answer -= 1
        time = requrirements[i][0]
        position = requrirements[i][1]
    answer += m-time
    print(answer)