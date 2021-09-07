def bs(array, num):
    value = array[int(len(array) / 2)]
    if len(array) == 1 and value != num:
        print("값이 없습니다.")
        return 0
    if value == num:
        print("값이 있습니다.")
        return 0
    else:
        if value > num:
            bs(array[0:int(len(array)/2)], num)
        else:
            bs(array[int(len(array)/2):len(array)+1], num)


n = list(map(int, input().split()))
n.sort()
print("찾을 수를 입력하세요")
find = int(input())
bs(n, find)
