from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n)
        dp[n-1] = 0
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                dp[i] = float('inf')
            else:
                end = min(n - 1, i + nums[i])
                for j in range(i + 1, end + 1):
                    dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]

        '''
        n = len(nums)
        @cache
        def _jump(i):
            if i == n - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            best = float('inf')
            end = min(n - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                best = min(best, 1 + _jump(j))
            # for j in range(1, nums[i] + 1):
            #     if i + j < n:
            #         best = min(best, 1 + _jump(i + j))
            return best
        return _jump(0)
        '''