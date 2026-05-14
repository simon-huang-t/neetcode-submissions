class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if height[l] < height[r]:
                if left_max < height[l]:
                    left_max = height[l]
                else:
                    max_area += left_max - height[l]
                l += 1

            else:
                if right_max < height[r]:
                    right_max = height[r]
                else:
                    max_area += right_max - height[r]
                r -= 1

        return max_area
