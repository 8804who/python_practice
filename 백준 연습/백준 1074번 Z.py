import sys


def search(rowStart, rowEnd, colStart, colEnd, size):
    global count
    if size == 1:
        count += 1
        if rowStart == r and colStart == c:
            print(count, end="")
    else:
        if r > (rowStart+size//2)-1:
            count += ((size//2)**2)*2
            if c > (colStart+size//2)-1:
                count += (size//2)**2
                search((rowEnd-size//2)+1, rowEnd, (colEnd-size//2)+1, colEnd, size//2)
            else:
                search((rowEnd-size//2)+1, rowEnd, colStart, (colStart+size//2)-1, size//2)
        else:
            if c > (colStart+size//2)-1:
                count += (size//2)**2
                search(rowStart, (rowStart+size//2)-1, (colEnd-size//2)+1, colEnd, size//2)
            else:
                search(rowStart, (rowStart+size//2)-1, colStart, (colStart+size//2)-1, size//2)


N, r, c = map(int, sys.stdin.readline().split())
count = -1
search(0, 2**N-1, 0, 2**N-1, 2**N)