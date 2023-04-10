import sys
input = sys.stdin.readline
N = int(input())
hangers = tuple(map(int, input().split()))

hanger_nums = [0, 0, 0]
for hanger in hangers:
    hanger_nums[hanger-1] += 1

U, D = map(int, input().split())
possible = True
answer = []
for hanger in hangers:
    if hanger == 1:
        hanger_nums[0] -= 1
        if U > 0:
            U -= 1
        else:
            possible = False
        answer.append("U")
    elif hanger == 2:
        hanger_nums[1] -= 1
        if D > 0:
            D -= 1
        else:
            possible = False
        answer.append("D")
    elif hanger_nums[0] < U:
        U -= 1
        answer.append("U")
    elif hanger_nums[1] < D:
        D -= 1
        answer.append("D")
    else:
        if U > D:
            U -= 1
            answer.append("U")
        else:
            D -= 1
            answer.append("D")

if possible:
    print("YES")
    for a in answer:
        print(a, end='')
else:
    print("NO")