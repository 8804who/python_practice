n = int(input())
count = 0
i = 0
while n > count:
    i += 1
    count += i
num = i+1
order = i-(count-n)
if i % 2 == 0:
    print(order, "/", num-order,sep="")
else:
    print(num-order, "/", order, sep="")