from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def _rob(i):
            if i >= n:
                return 0
            return max(_rob(i + 1), nums[i] + _rob(i + 2))
            
        return _rob(0)