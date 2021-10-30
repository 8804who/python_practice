N, M, B = map(int, input().split())
field = []
minTime = 999999999
maxHigh = 0
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        field.append(temp[j])
for i in range(min(field), max(field)+1):
    inventory = B
    time = 0
    for j in range(len(field)):
        if field[j] > i:
            inventory += field[j]-i
            time += (field[j]-i)*2
        elif field[j] < i:
            inventory -= i-field[j]
            time += i-field[j]
    if inventory >= 0:
        if time <= minTime:
            minTime = time
            if maxHigh < i:
                maxHigh = i
print(minTime, maxHigh)