class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_linear(l, r):
            prev = prev_prev = 0
            for i in range(l, r):
                prev_prev, prev = prev, max(nums[i] + prev_prev, prev)
            return prev
        return max(rob_linear(1, n), rob_linear(0, n - 1))