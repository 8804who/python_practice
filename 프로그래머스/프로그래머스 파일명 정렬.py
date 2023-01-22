def solution(files):
    answer = []
    fileName=[]
    idx=0
    for file in files:
        head=''
        number=''
        tail=''
        isTail=False
        for i in file:
            if not isTail:
                if 57>=ord(i)>=48:
                    number+=i
                    continue
                elif number!='':
                    isTail=True
                    tail+=i
                    continue
                elif 90>=ord(i)>=65:
                    head+=chr(ord(i)+32)
                    continue
                head+=i
            else:
                tail+=i
        fileName.append([head, number, tail, idx])
        idx+=1
    fileName.sort(key = lambda x: (x[0], int(x[1])))
    for i in fileName:
        answer.append(files[i[3]])
    return answer