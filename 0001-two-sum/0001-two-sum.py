class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            if target - n in dic:
                return [dic[target - n], i]
            dic[n] = i
# Time - O(n)
# Space - O(n)
# Brute - compare each number with every other to check if their sum is equal to target but time will be n square
        
        
        
        