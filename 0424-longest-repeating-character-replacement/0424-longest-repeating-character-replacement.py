class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        max_length = 0
        char_frequency = {}
        max_repeat_letter_count = 0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
            max_repeat_letter_count = max(max_repeat_letter_count, char_frequency[right_char])
            if window_end - window_start + 1 - max_repeat_letter_count > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
        