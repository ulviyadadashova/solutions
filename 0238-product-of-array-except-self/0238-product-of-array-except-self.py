class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for num in nums:
            ans.append(ans[-1] * num)
        multiply = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= multiply
            multiply *= nums[i]
        return ans[:-1]


        