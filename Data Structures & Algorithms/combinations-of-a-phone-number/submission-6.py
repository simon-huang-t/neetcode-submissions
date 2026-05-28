'''
Possible int to str instead of str:str?
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        n = len(digits)
        def backtrack(i, track):
            if len(track) == n:
                res.append(''.join(track))
                return
            letters = digitsToLetters[digits[i]]
            for c in letters:
                track.append(c)
                backtrack(i + 1, track)
                track.pop()
        if digits:
            backtrack(0, [])
        return res