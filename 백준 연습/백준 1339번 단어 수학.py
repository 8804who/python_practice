from string import ascii_uppercase
N = int(input())
Word = []
AlphabetCount = [0]*10
Alphabet = []
Sum = 0
for i in range(N):
    Word.append(list(input()))
    for Spelling in ascii_uppercase:
        if Word[i].count(Spelling)>0 and Spelling not in Alphabet:
            Alphabet.append(Spelling)
for i in range(N):
    for j in range(0, len(Word[i])):
        for k, Spelling in zip(range(len(Alphabet)), Alphabet):
            AlphabetCount[k] += Word[i][j].count(Spelling)*(10**(len(Word[i])-j-1))
AlphabetCount.sort(reverse=True)
for i in range(10):
    Sum += AlphabetCount[i]*(9-i)
print(Sum)
