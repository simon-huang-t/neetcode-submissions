class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def backtrack(start, track):
            res.append(track[:])
            for i in range(start, n):
                if i > start and nums[i - 1] == nums[i]:
                    continue
                track.append(nums[i])
                backtrack(i+1, track)
                track.pop()

        backtrack(0, [])
        return res