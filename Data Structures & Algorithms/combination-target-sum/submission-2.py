class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(start, total, track):
            if total == target:
                res.append(track[:])
                return
            # if start == n: #This is false. Unlimited choice
            if total > target:
                return
            for i in range(start, n):
                track.append(nums[i])
                backtrack(i, total + nums[i], track)
                track.pop()
        backtrack(0, 0, [])
        return res