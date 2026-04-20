import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))
    special_indice = int(input())-1

    target = nums[special_indice]

    forward = 0
    backward = 0

    for i in range(special_indice):
        if forward%2 == 0 and nums[i] != target:
            forward+=1
        elif forward%2 == 1 and nums[i] == target:
            forward+=1

    for i in range(n-1, special_indice, -1):
        if backward%2 == 0 and nums[i] != target:
            backward+=1
        elif backward%2 == 1 and nums[i] == target:
            backward+=1

    answer = max(forward, backward)
    if answer%2==1:
        answer += 1

    print(answer)
    