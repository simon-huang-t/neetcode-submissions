class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtracking(start, track):
            res.append(track[:])
            if start == n:
                return
            for i in range(start, n):
                track.append(nums[i])
                backtracking(i + 1, track)
                track.pop()
        
        backtracking(0, [])
        return res