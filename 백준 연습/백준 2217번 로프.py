import sys
inp = sys.stdin.readline
N = int(inp())
rope = []
weight = 0
max_weight = 0
for i in range(N):
    rope.append(int(inp()))
rope.sort(reverse=True)
for i in range(N):
    weight = rope[i]*(i+1)
    if max_weight <= weight:
        max_weight = weight
print(max_weight)