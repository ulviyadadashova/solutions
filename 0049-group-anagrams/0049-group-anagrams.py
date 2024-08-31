class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in dict:
                dict[sorted_word].append(word)
            else:
                dict[sorted_word] = [word]
        return dict.values()

        