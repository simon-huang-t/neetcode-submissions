class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        initial_lock = '0000'
        deadends = set(deadends)
        possibilities = (-1, 1)
        if initial_lock in deadends:
            return -1
        queue = deque([initial_lock])
        visited = set({initial_lock})
        turns = 0
        while queue:
            for _ in range(len(queue)):
                lock = queue.popleft()
                if lock == target:
                    return turns
                for i, digit in enumerate(lock):
                    for possibility in possibilities:
                        new_digit = (int(digit) + possibility) % 10
                        new_lock = lock[:i] + str(new_digit) + lock[i+1:]
                        if new_lock not in deadends and new_lock not in visited:
                            queue.append(new_lock)
                            visited.add(new_lock)
            turns += 1
        return -1
