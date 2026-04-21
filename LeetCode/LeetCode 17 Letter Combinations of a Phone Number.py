from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [['a', 'b', 'c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']]
        
        q = deque([('',0)])

        answer = []
        while q:
            text, idx = q.popleft()

            if idx == len(digits)-1:
                for letter in letters[int(digits[idx])-2]:
                    answer.append(text+letter)
            else:
                for letter in letters[int(digits[idx])-2]:
                    q.append((text+letter, idx+1))
        
        return answer