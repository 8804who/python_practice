class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        p = 0
        for i in range(len(nums)-2):
            if nums[i] > nums[i+1]:
                if p >= 1:
                    return False
                p += 1
                if nums[i] <= nums[i+2]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]

        if nums[-1] < nums[-2]:
            if p >= 1:
                return False
            else:
                nums[-1] = 10000

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False

        return True