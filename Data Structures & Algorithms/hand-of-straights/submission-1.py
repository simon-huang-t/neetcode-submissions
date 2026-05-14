class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        hand.sort()
        for i, num in enumerate(hand):
            if counter[num] == 0:
                continue
            # counter[num] -= 1
            # length = 1
            for j in range(groupSize):
                if counter[num + j] == 0:
                    return False
                counter[num + j] -= 1
                # length += 1
        return True
                