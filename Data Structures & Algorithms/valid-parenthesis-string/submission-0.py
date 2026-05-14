class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = leftMax = 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin = max(0, leftMin - 1)
                leftMax -= 1
                if leftMax < 0:
                    return False
            else: #'*'
                leftMin = max(0, leftMin - 1)
                leftMax += 1
        return leftMin == 0
