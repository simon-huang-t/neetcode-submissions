from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def _canPartition(i, target):
            if target == 0:
                return True
            if i == n or target < 0:
                return False
            return _canPartition(i + 1, target) or _canPartition(i + 1, target - nums[i])
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        return _canPartition(0, target)
        