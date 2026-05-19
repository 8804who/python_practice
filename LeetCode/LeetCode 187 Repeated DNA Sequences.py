class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        substr_set = set()
        for i in range(len(s)-9):
            substr = s[i:i+10]
            if substr in substr_set:
                answer.add(substr)
            else:
                substr_set.add(substr)
        
        return list(answer)