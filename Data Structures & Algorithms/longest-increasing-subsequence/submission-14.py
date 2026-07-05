import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bisect_left(arr, target):
            l, r = 0, len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        dp = []
        for num in nums:
            # idx = bisect.bisect_left(dp, num)
            idx = bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)
