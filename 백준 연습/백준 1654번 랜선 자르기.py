import sys
N, M = map(int, sys.stdin.readline().split())
cable = []
for i in range(N):
    cable.append(int(sys.stdin.readline()))
start = 1
final = max(cable)
max_length = 0
while start <= final:
    count = 0
    length = (start+final)//2
    for i in range(len(cable)):
        count += cable[i]//length
    if count >= M and max_length < length:
        max_length = length
    if count >= M:
        start = length+1
    else:
        final = length-1
print(max_length, end='')