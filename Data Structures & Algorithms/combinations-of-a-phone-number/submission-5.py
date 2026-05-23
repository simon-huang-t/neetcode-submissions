class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToChar = {
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
        def backtrack(start, track):
            if len(track) == len(digits):
                res.append(''.join(track))
                return
            letter = digits[start]
            for char in digitsToChar[letter]:
                track.append(char)
                backtrack(start + 1, track)
                track.pop()
        if digits:
            backtrack(0, [])
        return res