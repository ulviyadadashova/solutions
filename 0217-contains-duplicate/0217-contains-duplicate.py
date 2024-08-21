class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num in dict:
                return True
            else:
                dict[num] = 0
        return False
        