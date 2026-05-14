class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort() #
        def backtrack(start, total, track):
            if total == target:
                res.append(track[:])
                return
            if total > target:
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]: #
                    continue #
                track.append(candidates[i])
                backtrack(i + 1, total + candidates[i], track) #
                track.pop()
        backtrack(0, 0, [])
        return res