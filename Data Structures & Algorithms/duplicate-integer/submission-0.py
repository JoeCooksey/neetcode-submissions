class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set(nums)
        return len(nums) != len(uniqueNums)