class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        INF = 1<<32
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            return 0 if nums[0] > nums[1] else 1
        s = 1
        e = len(nums)

        nums = [-INF]+nums+[-INF]

        while s <= e:
            mid = (s+e)//2

            if nums[mid-1] < nums[mid]:
                if nums[mid] > nums[mid+1]:
                    return mid-1
                else:
                    s = mid+1
            elif nums[mid-1] > nums[mid]:
                e = mid-1
            else:
                s = mid+1