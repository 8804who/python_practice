num = int(input())
name = []
result = ""
for i in range(num):
    name.append(input())
if name[0] < name[1]:
    result = "INCREASING"
    for i in range(1, num-1):
        if name[i] > name[i+1]:
            result = "NEITHER"
            break
else:
    result = "DECREASING"
    for i in range(1, num-1):
        if name[i] < name[i+1]:
            result = "NEITHER"
            break
print(result)