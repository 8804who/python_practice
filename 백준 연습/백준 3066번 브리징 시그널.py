import sys
from bisect import bisect_left as bs


T = int(sys.stdin.readline())
for test_case in range(T):
    N = int(sys.stdin.readline())

    nums = [int(sys.stdin.readline()) for _ in range(N)]
    lis = [nums[0]]
    for num in nums[1:]:
        if num>lis[-1]:
            lis.append(num)
        else:
            lis[bs(lis, num)] = num
    print(len(lis))
