class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Tempetature, index
        n = len(temperatures)
        res = [0] * n
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([temperature, i])
        return res