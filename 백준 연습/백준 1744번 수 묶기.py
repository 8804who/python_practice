import sys
positive_num=[]
negative_num=[]
sum = 0
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n > 0:
        positive_num.append(n)
    else:
        negative_num.append(n)
positive_num.sort()
negative_num.sort()
while len(positive_num) > 0:
    if len(positive_num) > 1:
        if positive_num[-1] > 1 and positive_num[-2]>1:
            sum += positive_num.pop()*positive_num.pop()
        else:
            sum += positive_num.pop()
    else:
        sum += positive_num.pop()
while len(negative_num) > 0:
    if len(negative_num) > 1:
        sum += negative_num.pop(0)*negative_num.pop(0)
    else:
        sum+=negative_num.pop(0)
print(sum)