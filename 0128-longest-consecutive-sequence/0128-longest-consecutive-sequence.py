class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                max_length = max(max_length, length)
        return max_length








        