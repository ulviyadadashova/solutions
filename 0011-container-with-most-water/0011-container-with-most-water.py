class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, (min(height[l], height[r])) * (r - l))
            if height[l] >= height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
        return max_area

# Time - O(n)
# Space - O(1)
# Brute - two nested loops second in reversed order and save the max area found but time is O(n square)



        