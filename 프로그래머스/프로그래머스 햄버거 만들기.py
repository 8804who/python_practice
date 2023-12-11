def solution(ingredient):
    answer = 0
    string = ''
    for char in ingredient:
        string+=str(char)
        if len(string) >= 4 and string[-4:] == '1231':
            answer += 1
            string = string[:-4]
    return answer