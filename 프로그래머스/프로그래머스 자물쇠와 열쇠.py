def solution(key, lock):
    answer = False
    lockSize = len(lock)
    up = 0
    down = lockSize - 1
    left = 0
    right = lockSize - 1

    k = [[0 for _ in range(len(key) * 3)] for _ in range(len(key) * 3)]
    for i in range(len(key)):
        for j in range(len(key)):
            k[i + len(key)][j + len(key)] = key[i][j]
    key = k

    for i in range(lockSize):
        empty = False
        for j in range(lockSize):
            if lock[i][j] == 0:
                empty = True
        if empty:
            break
        up += 1
    for i in range(lockSize - 1, -1, -1):
        empty = False
        for j in range(lockSize):
            if lock[i][j] == 0:
                empty = True
        if empty:
            break
        down -= 1
    for i in range(lockSize):
        empty = False
        for j in range(up, down + 1):
            if lock[j][i] == 0:
                empty = True
        if empty:
            break
        left += 1
    for i in range(lockSize - 1, -1, -1):
        empty = False
        for j in range(up, down + 1):
            if lock[j][i] == 0:
                empty = True
        if empty:
            break
        right -= 1
    while up - down > left - right:
        if up > 0:
            up -= 1
            continue
        if down < lockSize - 1:
            down += 1
    while up - down < left - right:
        if left > 0:
            left -= 1
            continue
        if right < lockSize - 1:
            right += 1

    length = down - up + 1
    keySize = len(key)
    for i in range(0, keySize - length + 1):
        for j in range(0, keySize - length + 1):
            arr = [[0 for _ in range(length)] for _ in range(length)]
            for h in range(i, i + length):
                for w in range(j, j + length):
                    arr[h - i][w - j] = key[h][w]
            for r in range(4):
                arr = rotate(arr)
                openable = True
                for h in range(length):
                    for w in range(length):
                        if arr[h][w] == lock[up + h][left + w]:
                            openable = False
                            break
                if openable:
                    answer = True
    return answer


def rotate(arr):
    rotateArr = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            rotateArr[j][len(arr) - 1 - i] = arr[i][j]
    return rotateArr