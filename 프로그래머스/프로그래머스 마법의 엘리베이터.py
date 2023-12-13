def solution(storey):
    answer = 0
    div = 1

    while storey > 0:
        n = storey % (div * 10)
        n //= div
        if n == 5:
            temp_storey = storey - n * div
            if temp_storey == 0:
                answer += n
                storey -= n * (div)
            else:
                temp_div = div * 10
                while temp_storey > 0:
                    temp_n = temp_storey % (temp_div * 10)
                    if temp_n == 5 * temp_div:
                        temp_storey -= temp_n
                        if temp_storey == 0:
                            answer += n
                            storey += n * (div)
                        temp_div *= 10

                    elif temp_n > 5 * temp_div:
                        answer += n
                        storey += n * (div)
                        break
                    else:
                        answer += n
                        storey -= n * (div)
                        break
        elif n > 5:
            answer += 10 - n
            storey += (10 - n) * (div)
        else:
            answer += n
            storey -= n * (div)
        div *= 10
    return answer