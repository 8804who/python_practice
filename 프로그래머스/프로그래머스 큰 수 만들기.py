def solution(number, k):
    answer = ''
    count = 0
    index = 1
    while True:
        if number[index-1]<number[index]:
            number=number[:index-1]+number[index:]
            count+=1
            if index>1:
                index-=1
        else:
            index+=1
        if count==k or index==len(number):
            break
    if count!=k:
        number=number[:len(number)-(k-count)]
    return number