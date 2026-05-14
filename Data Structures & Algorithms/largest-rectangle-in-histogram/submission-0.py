class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] #sentinel
        max_area = 0
        for i, h in enumerate(heights):
            while stack[-1] != - 1 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] -  1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        n = len(heights)
        while stack[-1] != - 1:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area