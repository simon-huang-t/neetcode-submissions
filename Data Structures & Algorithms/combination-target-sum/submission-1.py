class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(start, total, track):
            if total == target:
                res.append(track[:])
                return
            if total > target:
                return
            for i in range(start, n):
                track.append(nums[i])
                total += nums[i]
                backtrack(i, total, track)
                track.pop()
                total -= nums[i]
        backtrack(0, 0, [])
        return res