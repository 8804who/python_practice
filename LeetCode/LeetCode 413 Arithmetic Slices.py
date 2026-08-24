class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        a = 0
        l = 1
        answer = 0
        for i in range(1, len(nums)):
            if a != nums[i]-nums[i-1]:
                a = nums[i]-nums[i-1]
                l = 2
            else:
                l += 1
            
            if l >= 3:
                answer += l-2
        
        return answer
        