class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        window_start = 0
        char_frequency = {}
        max_length = 0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_frequency and window_start <= char_frequency[right_char]:
                window_start = char_frequency[right_char] + 1
            char_frequency[right_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
# Time - O(n)
# Space - O(n)
# Brute - Check all substrings using two nested loops. For each substring, check for duplicates using a set. but time is O(n square)
                

        

            

        