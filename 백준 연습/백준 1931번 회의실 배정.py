import sys
time = []
count = 1
for i in range(int(sys.stdin.readline())):
    time.append([])
    start, end = (map(int, sys.stdin.readline().split()))
    time[i].append(start)
    time[i].append(end)
time.sort(key=lambda x: (x[1], x[0]))
now = time[0][1]
for i in range(1, len(time)):
    if time[i][0] >= now:
        count += 1
        now = time[i][1]
print(count)
