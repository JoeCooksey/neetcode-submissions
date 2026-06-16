class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# Map to store: { number: its_index }
        seen = {}
        
        for i, num in enumerate(nums):
            remaining = target - num
            
            # Check if the complement is already in our dictionary
            if remaining in seen:
                # Return the index of the complement and the current index
                return [seen[remaining], i]
            
            # Otherwise, remember this number and its index
            seen[num] = i
            
        return []