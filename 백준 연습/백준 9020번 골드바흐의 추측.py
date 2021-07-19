import sys
n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
prime = [False, False]+[True]*9999
for i in range(2, 101):
    if prime[i]:
        j = i*2
        while j <= 10000:
            prime[j] = False
            j += i
for i in range(n):
    for j in range(int(num[i]/2)):
        if prime[int(num[i]/2)-j] and prime[int(num[i]/2)+j]:
            print(int(num[i]/2)-j, int(num[i]/2)+j)
            break