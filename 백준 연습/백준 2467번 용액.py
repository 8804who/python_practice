import sys
N = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))

first = 0
end = len(solution)-1
minNum = 1e14
s1 = 0
s2 = 0
while first < end:
    num = solution[first]+solution[end]
    if abs(num) < minNum:
        s1 = first
        s2 = end
        minNum = abs(num)
    if num > 0:
        end -= 1
    elif num < 0:
        first += 1
    else:
        break
print(solution[s1], solution[s2])