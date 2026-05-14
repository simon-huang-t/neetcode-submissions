class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = nums[-1]
        for i in range(n-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return True if goal == 0 else False