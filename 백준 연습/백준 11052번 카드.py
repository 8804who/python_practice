import sys
N = int(sys.stdin.readline())
price = [0]+list(map(int, sys.stdin.readline().split()))
for i in range(1, N+1):
    for j in range(1, i//2+1):
        price[i] = max(price[i], price[j]+price[i-j])
print(price[N], end="")