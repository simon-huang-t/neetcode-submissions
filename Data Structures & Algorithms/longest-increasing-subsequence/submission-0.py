from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def longest(i):
            if i == n:
                return 0
            LIS = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + longest(j))
            return LIS

        return max(longest(i) for i in range(n))
