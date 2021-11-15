import sys


def lotto(n, numArr):
    for select in range(len(numArr)):
        if select+1 != n:
            print(numArr[select], end=" ")
    print("")
    if n != 1:
        lotto(n-1, numArr)
    else:
        print("")


while True:
    input_num = list(map(int, sys.stdin.readline().split(" ")))
    if input_num[0] == 0:
        break
    arr = [0] * input_num[0]
    for i in range(input_num[0]):
        arr[i] = input_num[i+1]
    lotto(input_num[0], arr)
