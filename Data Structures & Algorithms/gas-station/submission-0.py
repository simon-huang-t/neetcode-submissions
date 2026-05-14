class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1
        n = len(gas)
        current_gas = 0
        res = 0
        for i in range(n):
            current_gas += (gas[i] - cost[i])
            if current_gas < 0:
                current_gas = 0
                res = i + 1
        return res

