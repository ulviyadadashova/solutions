class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        max_length = 0
        dic = {}
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in dic and window_start <= dic[right_char]:
                window_start = dic[right_char] + 1
            dic[right_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)
        return max_length

        