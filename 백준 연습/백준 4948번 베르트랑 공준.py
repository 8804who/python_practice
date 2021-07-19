import sys
n = []
while True:
    ans = int(sys.stdin.readline())
    if ans == 0:
        break
    n.append([ans])
prime = [False, False]+[True]*(max(map(max, n))*2-1)
for i in range(2, int(len(prime)**0.5)):
    if prime[i]:
        j = i
        while True:
            j += i
            if j > len(prime)-1:
                break
            prime[j] = False
for i in range(len(n)):
    for j in range(n[i][0]+1, n[i][0]*2+1):
        if prime[j]:
            n[i].append(j)
for i in range(len(n)):
    print(len(n[i])-1)