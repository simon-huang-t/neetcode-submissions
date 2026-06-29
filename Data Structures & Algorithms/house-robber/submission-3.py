class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])
        # prev_prev, prev = nums[0], max(nums[0], nums[1])
        prev_prev = prev = 0
        for i in range(n):
        # for i in range(2, n):
            prev_prev, prev = prev, max(nums[i] + prev_prev, prev)
        return prev

