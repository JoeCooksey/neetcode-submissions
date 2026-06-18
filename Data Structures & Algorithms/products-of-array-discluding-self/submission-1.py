import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solns = []
        #Iterate through array nums
        for i in range (0, len(nums)):
            #Take values before nums[i] and after
            prefix = nums[:i]
            suffix = nums[i+1:]
            #Append the solutions of all values multiplied with eachother
            solns.append(math.prod(prefix) * math.prod(suffix))
        return solns