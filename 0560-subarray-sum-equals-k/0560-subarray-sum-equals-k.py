class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        dic = {}
        dic[0] = 1
        for i in range(len(nums)):
            sum  += nums[i]
            if sum - k in dic:
                count += dic[sum - k]
            dic[sum] = dic.get(sum, 0) + 1      
        return count      
