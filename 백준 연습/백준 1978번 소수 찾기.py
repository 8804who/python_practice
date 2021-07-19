import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
prime = []
for i in range(n):
    if num[i] == 1:
        continue
    now = 1
    while now < num[i]:
        now += 1
        if num[i] % now == 0:
            break
    if now == num[i]:
        prime.append(num[i])
print(len(prime))