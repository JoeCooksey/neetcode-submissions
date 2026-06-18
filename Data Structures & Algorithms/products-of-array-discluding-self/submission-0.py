import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solns = []

        for i in range (0, len(nums)):
            prefix = nums[:i]
            suffix = nums[i+1:]
            solns.append(math.prod(prefix) * math.prod(suffix))
        return solns