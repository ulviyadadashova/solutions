class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0 )
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0 )
        return dict_t == dict_s
# Time - O(n)
# Space - O(n)
# Brute - sort the arrays then check if same but time is O(nlogn)


            
