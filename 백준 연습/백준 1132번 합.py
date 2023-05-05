import sys

N = int(sys.stdin.readline())
answer = 0
start = {}
char_to_num = {}
place_value_sum = [[0, i] for i in range(10)]
strings = []

for i in range(N):
    strings.append(sys.stdin.readline().rstrip())
    place_value = 1
    for char in strings[-1][::-1]:
        place_value_sum[ord(char)-65][0] += place_value
        place_value *= 10
    start[ord(strings[-1][0])-65] = 1

place_value_sum.sort()

for n in place_value_sum:
    if n[1] not in start:
        char_to_num[n[1]] = 0
        break

num = 1
for n in place_value_sum:
    if n[1] not in char_to_num:
        char_to_num[n[1]] = num
        num += 1

for string in strings:
    place_value = 1
    for char in string[::-1]:
        answer += char_to_num[ord(char)-65] * place_value
        place_value *= 10
print(answer)