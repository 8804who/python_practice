from collections import deque

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        q=deque()

        q.append(([],0))
        answer = set()
        while q:
            subset, idx = q.popleft()
            answer.add(tuple(subset))
            idx += 1
            if idx > len(nums):
                continue
            q.append((subset+[nums[idx-1]],idx))
            q.append((subset,idx))
    
        return [list(a) for a in answer]