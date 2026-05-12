from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)
        end = bisect_right(nums, target)

        if start >= len(nums):
            return [-1, -1]

        if nums[start] != target:
            start += 1
        end -= 1
        
        if nums[end] != target:
            return [-1, -1]
        return [start, end]