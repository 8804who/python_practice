N = int(input())

words = [input() for _ in range(N)]

words.sort(key=lambda x:-len(x))

x_set = []

for word in words:
    okay = True
    for x in x_set:
        if x[:len(word)] == word:
            okay = False
            break
    if okay:
        x_set.append(word)

print(len(x_set))