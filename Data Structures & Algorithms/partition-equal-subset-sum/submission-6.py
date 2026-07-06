class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = set()
        dp.add(0)
        n = len(nums)
        # for i in range(n - 1, - 1, -1):
        for i, num in enumerate(nums):
            nextDP = set()
            for t in dp:
                if t + num == target:
                    return True
                nextDP.add(t + num)
                nextDP.add(t)
            dp = nextDP
        return False