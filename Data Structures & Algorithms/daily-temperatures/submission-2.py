class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #(ind, temperature)
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                stackIdx, _ = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append((i, temperature))
    
        return res
