from copy import deepcopy
from random import shuffle

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.current = deepcopy(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffle(self.current)
        return self.current



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()