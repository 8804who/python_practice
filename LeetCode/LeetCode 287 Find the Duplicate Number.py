class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = [0] * 100001

        for num in nums:
            if check[num] == 1:
                return num
            check[num] += 1