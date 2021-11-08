import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
pl, mi, mu, di = map(int, sys.stdin.readline().split())
count = 0

for i in range(4):
    for j in range(3):
        for k in range(2):
            arr = [1, 2, 3, 4]
            print(arr.pop(i), end="")
            print(arr.pop(j), end="")
            print(arr.pop(k), end="")
            print(arr.pop())

while count < (N-1)*(N-2):
    arr = [1, 2, 3, 4]
    n = len(arr)
    while len(arr) > 0:
        print(arr.pop(n))
        n -= 1