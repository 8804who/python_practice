T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    distance = y-x
    move = 0
    count = 0
    while distance > 0:
        if distance >= ((move+1)*(move+2))/2:
            move += 1
        elif distance < (move*(move+1))/2 and move > 1:
            move -= 1
        distance -= move
        count += 1
    print(count)