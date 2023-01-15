def solution(phone_book):
    answer = True
    num = dict()
    for phone in phone_book:
        for i in range(1, len(phone) + 1):
            if phone[0:i] not in num:
                num[phone[0:i]] = 1
            else:
                num[phone[0:i]] += 1

    for phone in phone_book:
        if num[phone] > 1:
            answer = False
    return answer