class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(track):
            if len(track) == n:
                res.append(track[:])
                return
            for num in nums:
                if num in track:
                    continue
                track.append(num)
                backtrack(track)
                track.pop()
        backtrack([])
        return res