class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in group:
                group[sorted_word].append(word)
            else:
                group[sorted_word] = [word]
        return list(group.values())
# Time - O(n * klogk)
# Space - O(nk)
# Brute - get every pair of words sort them and compare if they are anagrams time will be n square * klogk
