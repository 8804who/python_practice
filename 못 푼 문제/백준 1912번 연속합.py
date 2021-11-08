import sys
n = int(sys.stdin.readline())
con_sum = [0]*(n+1)

input_num = list(map(int, sys.stdin.readline().split()))
for i in range(1, n+1):
    con_sum[i] = con_sum[i-1]+input_num[i-1]

max_idx = 1
max_num = con_sum[1]
for i in range(2, n+1):
    if max_num < con_sum[i]:
        max_num = con_sum[i]
        max_idx = i
min_num = con_sum[1]
for i in range(2, max_idx):
    if min_num > con_sum[i]:
        min_num = con_sum[i]
print(con_sum)
print(max_num, min_num)
print(max_num-min_num)