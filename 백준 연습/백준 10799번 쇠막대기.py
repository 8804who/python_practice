import sys

input_data = list(map(str, sys.stdin.readline()[:-1]))
count, stick, pivot = 0, 0, 0
while pivot < len(input_data):
    if pivot < len(input_data) - 2:
        if input_data[pivot] == "(" and input_data[pivot + 1] == ")":
            count += stick
            pivot += 1
        elif input_data[pivot] == "(":
            stick += 1
        elif input_data[pivot] == ")":
            stick -= 1
            count += 1
    else:
        if input_data[pivot - 1] == "(":
            count += stick
        else:
            count += 1
    pivot += 1
print(count)
