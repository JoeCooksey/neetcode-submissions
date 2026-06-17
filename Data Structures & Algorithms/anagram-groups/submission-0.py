from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create map for anagrams
        anagram_map = defaultdict(list)

        #iterate through strs
        for word in strs:
            #Create key of the sorted word
            sorted_word = "".join(sorted(word))
            #Compare with the key and if matched, map to same key
            anagram_map[sorted_word].append(word)
        #Return the unique word values in arrays based on their keys
        return list(anagram_map.values())
        