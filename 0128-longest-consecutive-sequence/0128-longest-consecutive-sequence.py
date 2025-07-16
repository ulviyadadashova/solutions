class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        numSet = set(nums)
        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                max_length = max(max_length, length)
        return max_length
# Time - O(n)
# Space - O(n)
# Brute - sort the array and check if next number is 1 unit more if yes increase size and keep track of maximum length time is O(nlogn)




        