class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        apply_operator = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: b - a,
            '*': lambda a, b: a * b,
            '/': lambda a, b: b / a,
        }
        stack = []
        for token in tokens:
            if token in apply_operator:
                a = stack.pop()
                b = stack.pop()
                token = apply_operator[token](a, b)
            stack.append(int(token))
        return stack[0]