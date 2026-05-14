class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [0, 0, 0]
        for triplet in triplets:
            a, b, c = triplet
            targetA, targetB, targetC = target
            if a > targetA or b > targetB or c > targetC:
                continue
            if a == targetA:
                found[0] = 1
            if b == targetB:
                found[1] = 1
            if c == targetC:
                found[2] = 1

        return found == [1, 1, 1]