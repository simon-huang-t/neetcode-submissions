class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = set()
        dp.add(0)
        for i, num in enumerate(nums):
            new_dp = set()
            for t in dp:
                if t + num == target:
                    return True
                new_dp.add(t+num)
                new_dp.add(t)
            dp = new_dp
        return False