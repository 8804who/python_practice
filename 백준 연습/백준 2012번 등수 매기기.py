import sys
n= int(input())
rank = []
sum = 0
for i in range(n):
    rank.append(int(sys.stdin.readline()))
rank.sort()
for i in range(n):
    sum += abs(rank[i]-(i+1))
print(sum)