class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums)-1
        while idx > 0:
            if nums[idx] > nums[idx-1]:
                idx -= 1
                break
            idx -= 1
        if idx == 0:
            if len(nums) == 1:
                return
            if nums[0] >= nums[1]:
                nums.reverse()
                return

        for i in range(len(nums)-1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break
 
        for i in range(len(nums)-1, idx, -1):
            for j in range(idx+1, i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]