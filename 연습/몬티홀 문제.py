import random


def monty_hall():
    option_list = ['a', 'b', 'c']
    correct = random.choice(option_list)
    print("답을 선택하십시오")
    print("1.a 2.b 3.c")
    my_choice = input()
    while True:
        open_choice = random.choice(option_list)
        if open_choice != correct and open_choice != my_choice:
            break
    option_list.remove(open_choice)
    print(open_choice, "은 오답입니다.")
    print("선택을 변경하시겠습니까?")
    print("1.Y 2.N")
    change = int(input())
    if change == 1:
        if my_choice == option_list[0]:
            my_choice = option_list[1]
        else:
            my_choice = option_list[0]
    if my_choice == correct:
        print("정답입니다.")
    else:
        print("오답입니다. 정답은 ", correct, "입니다.")


monty_hall()
