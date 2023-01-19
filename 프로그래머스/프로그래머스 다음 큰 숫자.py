def solution(n):
    count1=bin(n).count('1')
    while True:
        n+=1
        if bin(n).count('1')==count1:
            break
    return n