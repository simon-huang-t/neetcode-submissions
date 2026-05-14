class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted((p, s) for p, s in zip(position, speed))[::-1]
        stack = []
        for p, s in pairs:
            stack.append((target - p) / s)
            while len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
