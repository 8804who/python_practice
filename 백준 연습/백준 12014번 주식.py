import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T+1):
    print("Case #", test_case, sep='')
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    lis = [arr[0]]

    for num in arr[1:]:
        start = 0
        end = len(lis)-1
        if lis[-1] < num:
            lis.append(num)
            continue
        idx = -1
        while start <= end:
            mid = (start+end)//2
            if lis[mid] >= num:
                idx = mid
                end = mid - 1
            else:
                start = mid + 1
        if idx != -1:
            lis[idx] = num

    if len(lis) >= K:
        print(1)
    else:
        print(0)
