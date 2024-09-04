class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            num = nums[i % n]
            while stack and num > nums[stack[-1]]:
                index = stack.pop()
                res[index] = num
            if i < n:
                stack.append(i)
        return res
                

        