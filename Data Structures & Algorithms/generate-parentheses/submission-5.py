class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        track = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(track))
                return
            if openN < n:
                track.append('(')
                backtrack(openN + 1, closedN)
                track.pop()
            if closedN < openN:
                track.append(')')
                backtrack(openN, closedN + 1)
                track.pop()
                        
        backtrack(0, 0)
        return res