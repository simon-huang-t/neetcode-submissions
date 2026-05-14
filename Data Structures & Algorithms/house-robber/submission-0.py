class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        prev_prev = nums[0]
        prev = max(nums[0], nums[1])
        for i in range(2, n):
            prev_prev, prev = prev, max(prev, prev_prev + nums[i])
        return prev