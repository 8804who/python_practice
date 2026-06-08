class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        start, end = 0, 0
        total_num = nums[0]
        length = len(nums)
        answer = length

        while True:
            if total_num >= target:
                if answer > end-start+1:
                    answer = end-start+1
                total_num -= nums[start]
                start += 1
            else:
                end += 1
                if end == length:
                    break
                total_num += nums[end]

        return answer
        