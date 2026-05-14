class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(start, track, total):
            if total == target:
                res.append(track[:])
                return
            if total > target:
                return
            for i in range(start, n):
                track.append(nums[i])
                backtrack(i, track, total + nums[i])
                track.pop()

        backtrack(0, [], 0)
        return res