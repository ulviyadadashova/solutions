class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        currMin = float('inf')
        while start < end:
            mid = start + (end - start) // 2
            currMin = min(currMin, nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return min(currMin, nums[start])

        