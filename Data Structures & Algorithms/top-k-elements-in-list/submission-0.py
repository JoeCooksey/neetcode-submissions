from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap with key as the value and count as the room
        frequencyMap = Counter(nums)
        # Find out the k most frequent values
        topValues = frequencyMap.most_common(k)
        # Extract the values of highesst frequency
        result = [num for num, count in topValues]
        return result