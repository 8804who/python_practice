import sys
array=[]
for i in range(int(sys.stdin.readline())):
    array.append(int(sys.stdin.readline()))
array.sort()
for i in range(len(array)):
    print(array[i])