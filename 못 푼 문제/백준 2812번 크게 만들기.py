N, K = map(int, input().split())
n = str(input())
num = []
count = []
for i in range(N):
    num.append(int(n[i]))
max_num = max(num[0:K])
for i in range(K):
    if num[i] < max_num:
        count.append(i)
if len(count) > 0:
    print(num[count[-1]:count[-1]+K-len(count)+1])
for i in range(len(num)):
    if i not in count:
        print(num[i], end="")