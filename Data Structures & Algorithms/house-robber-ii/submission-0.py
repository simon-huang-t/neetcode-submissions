class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def rob_linear(l, r):
            prev_prev = nums[l]
            prev = max(nums[l], nums[l + 1])
            for i in range(l + 2, r):
                prev_prev, prev = prev, max(prev, prev_prev + nums[i])
            return prev

        
        skip_first = rob_linear(1, n)
        skip_last = rob_linear(0, n - 1)
        return max(skip_first, skip_last)
