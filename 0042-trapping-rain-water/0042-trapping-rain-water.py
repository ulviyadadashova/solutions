class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

# Time - O(n)
# Space - O(1)
# Brute - 
# \U0001f511 The Core Idea:
# At any index i, the maximum height of water that can sit at i is determined by:

# The tallest bar to the left (leftMax)

# The tallest bar to the right (rightMax)

# Water cannot rise higher than the shorter of those two barriers.

# So, the water level at i is:
# Edit
# min(leftMax, rightMax)
# But there's already a bar of height height[i] there.
# So, the amount of water trapped at i is:
# water_at_i = min(leftMax, rightMax) - height[i]