class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#  Time - O(n)
# Space -  O(n)
# Brute force - two nested loops comparing each number with ever other number in arrar. time - O(n square)
