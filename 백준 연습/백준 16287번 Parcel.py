import sys

input = sys.stdin.readline

w, n = map(int, input().split())

arr = [-1] * (w+1)
arr2 = [-1] * (w+1)

nums = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1, n):
        total = nums[i]+nums[j]
        if total > w:
            continue
        arr[total] = i
        arr2[total] = j

isEnd = False
for i in range(n):
    for j in range(i+1, n):
        if isEnd:
            break
        total = nums[i] + nums[j]
        if total > w:
            continue
        if arr[w-total] != -1 and arr[w-total] != i and arr2[w-total] != i and arr[w-total] != j and arr2[w-total] != j:
            print("YES")
            isEnd = True

if not isEnd:
    print("NO")