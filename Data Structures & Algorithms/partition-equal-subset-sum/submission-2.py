class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        n = len(nums)
        dp = set()
        dp.add(0) #sum 0 is always possible
        for i in range(n - 1, - 1, - 1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target: 
                    return True
                nextDP.add(nums[i] + t)
                nextDP.add(t)
            dp = nextDP
        # return True if target in dp else False
        return False