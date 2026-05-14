class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(start, track):
            res.append(track[:])
            for i in range(start, n):
                track.append(nums[i])
                backtrack(i + 1, track)
                track.pop()
        backtrack(0, [])
        return res