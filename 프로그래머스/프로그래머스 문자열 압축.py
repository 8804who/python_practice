def solution(s):
    answer = len(s)
    for i in range(1, len(s)+1):
        temp=''
        count=1
        string=''
        start=0
        end=i
        while end<len(s)+1:
            if temp==s[start:end]:
                count+=1
                start+=i
                end+=i
            else:
                if count>1:
                    string+=str(count)
                string+=temp
                temp=s[start:end]
                start+=i
                end+=i
                count=1
        if count>1:
            string+=str(count)
        string+=temp
        string+=s[start:]
        if answer>len(string):
            answer=len(string)
    return answer