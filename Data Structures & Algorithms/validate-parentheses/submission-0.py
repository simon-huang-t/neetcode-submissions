class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}' : '{'}
        for symbol in s:
            if symbol in ('(', '[', '{'):
                stack.append(symbol)
            else: # Closing parenthesis
                if not stack:
                    return False
                else:
                    if stack[-1] != closeToOpen[symbol]:
                        return False
                    else:
                        stack.pop()
        if stack:
            return False
        return True