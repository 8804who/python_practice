import sys
input = sys.stdin.readline


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


N = int(input())
parent = [i for i in range(N)]
x_arr = []
y_arr = []
z_arr = []

for i in range(N):
    x, y, z = map(int, input().split())
    x_arr.append((x, i))
    y_arr.append((y, i))
    z_arr.append((z, i))

x_arr.sort()
y_arr.sort()
z_arr.sort()

route = []

for i in range(N-1):
    route.append((abs(x_arr[i][0]-x_arr[i+1][0]), x_arr[i][1], x_arr[i+1][1]))
    route.append((abs(y_arr[i][0]-y_arr[i+1][0]), y_arr[i][1], y_arr[i+1][1]))
    route.append((abs(z_arr[i][0]-z_arr[i+1][0]), z_arr[i][1], z_arr[i+1][1]))
route.sort()
answer = 0

for cost, start, end in route:
    if find(start) != find(end):
        union(start, end)
        answer += cost
print(answer)