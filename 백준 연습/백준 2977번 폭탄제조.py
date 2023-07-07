import math
import sys
N, M = map(int, sys.stdin.readline().split())
parts = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
start = 0
end = 100000

while start <= end:
    mid = (start+end)//2
    price = 0
    for part in parts:
        need = part[0]*mid-part[1]
        if need <= 0:
            continue
        else:
            min_price = 1e6
            for i in range(10001):
                cost = part[3] * i + math.ceil(max(0, (need-part[2]*i))/part[4])*part[5]
                if cost < min_price:
                    min_price = cost
            price += min_price
    if price <= M:
        answer = mid
        start = mid+1
    else:
        end = mid-1
print(answer)