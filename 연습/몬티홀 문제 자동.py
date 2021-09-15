import random


def monty_hall():
    option_list = ['a', 'b', 'c']
    correct = random.choice(option_list)
    first_choice = random.choice(option_list)
    while True:
        open_choice = random.choice(option_list)
        if open_choice != correct and open_choice != first_choice:
            break
    option_list.remove(open_choice)
    if first_choice == correct:
        return True
        '''답을 안바꾼게 정답인 경우'''
    else:
        return False
        '''답을 바꾼게 정답인 경우'''


retain = 0
change = 0
for i in range(10000):
    if monty_hall():
        retain += 1
    else:
        change += 1
print("답을 유지한게 정답인 경우", retain, "답을 바꾼게 정답인 경우", change)
