from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        @cache
        def rob_linear(l, r):
            if l >= r:
                return 0
            return max(rob_linear(l + 1, r), nums[l] + rob_linear(l + 2, r))

        skip_first = rob_linear(1, n)
        skip_last = rob_linear(0, n - 1)
        return max(skip_first, skip_last)
