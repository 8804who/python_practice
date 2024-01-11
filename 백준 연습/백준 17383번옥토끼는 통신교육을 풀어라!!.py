N = int(input())
times = sorted(list(map(int, input().split())))

answer = 1e9
start = 0
end = 1e9

while start <= end:
    mid = (start+end)//2

    solving = []
    front_idx = 0
    back_idx = len(times) - 1
    time = mid
    can = True

    if not solving:
        solving.append(times[back_idx])
        back_idx -= 1
    if solving[0] > mid:
        solving.insert(0, times[front_idx])
        front_idx += 1

    while front_idx <= back_idx:
        solve = False
        if solving and solving[0] <= time:
            end_time = solving.pop(0)
            solve = True
            if not solving:
                solving.append(end_time+times[back_idx])
                back_idx -= 1
        else:
            can = False
            break
        if solving[0] > time+mid:
            solving.insert(0, time+times[front_idx])
            front_idx += 1
        else:
            solving.append(time+times[back_idx])
            back_idx -= 1
        time += mid

    for solved_time in solving:
        if solved_time > time:
            can = False
        else:
            time += mid
    if can:
        end = mid - 1
        if answer > mid:
            answer = mid
    else:
        start = mid + 1

print(int(answer))