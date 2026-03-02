import sys

input = sys.stdin.readline

t = int(input())

def getMex(nums):
    num = 0
    while True:
        if num not in nums:
            return num
        num += 1

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    answer = True

    for i in range(n):
        if getMex(nums[:i+1]) == getMex(nums[i+1:]):
            answer = False
        
    if answer:
        print("YES")
    else:
        print("NO")