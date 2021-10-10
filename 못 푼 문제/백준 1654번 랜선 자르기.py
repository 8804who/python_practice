import sys
N, M = map(int, sys.stdin.readline().split())
cable = []
for i in range(N):
    cable.append(int(sys.stdin.readline()))
start = 0
final = int(sum(cable)/M)
max_length = 0
while start <= final:
    print(start, final)
    count = 0
    length = int((start+final)/2)
    for i in range(len(cable)):
        count += int(cable[i]/length)
    if count == N and max_length < length:
        max_length = length
    if count >= N:
        start = length+1
    else:
        final = length-1
    print(start, final, count, length)
print(max_length)