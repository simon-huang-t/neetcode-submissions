class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x_map = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.x_map[x].add(y)
        

    def count(self, point: List[int]) -> int:
        x, y = point
        if x not in self.x_map:
            return 0
        res = 0
        for ny in self.x_map[x]:
            if ny == y:
                continue
            
            d = ny - y
            res += (
                self.points[(x, ny)] *
                self.points[(x - d, ny)] *
                self.points[(x - d, y)]
            )
            res += (
                self.points[(x, ny)] *
                self.points[(x + d, ny)] *
                self.points[(x + d, y)]
            )
        return res
