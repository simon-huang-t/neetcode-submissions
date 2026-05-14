class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            updated = False
            new_prices = prices[:]
            for s, d, p in flights:
                if prices[s] != float('inf') and prices[s] + p  < new_prices[d]:
                    new_prices[d] = prices[s] + p
                    updated = True
            prices = new_prices
            if not updated:
                break
        return prices[dst] if prices[dst] != float('inf') else -1



        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            updated = False
            new_prices = prices[:]
            for s, d, p in flights:
                if prices[s] != float('inf') and prices[s] + p < new_prices[d]:
                    new_prices[d] = prices[s] + p
                    updated = True
            prices = new_prices

            if not updated:
                break
        
        return prices[dst] if prices[dst] != float('inf') else -1