import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
total = 0
answer = sum(arr)+1
for i in arr:
    if i > total+1:
        answer = total+1
        break
    else:
        total += i
print(answer)
