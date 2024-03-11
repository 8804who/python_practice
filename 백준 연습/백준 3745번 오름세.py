import sys
from bisect import bisect_left as bs
try:
    while True:
        N = int(sys.stdin.readline())
        nums = list(map(int, sys.stdin.readline().split()))
        lis = [nums[0]]
        for num in nums[1:]:
            if num>lis[-1]:
                lis.append(num)
            else:
                lis[bs(lis, num)] = num
        print(len(lis))
except:
    exit()