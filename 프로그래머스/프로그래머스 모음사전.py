from itertools import product


def solution(word):
    products = []
    for i in range(1, 6):
        for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            st = ''
            for ch in p:
                st += ch
            products.append(st)
    products.sort()

    for i, st in enumerate(products):
        if st == word:
            return i + 1