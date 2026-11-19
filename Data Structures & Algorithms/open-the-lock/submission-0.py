class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        wheels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        initial_lock = '0000'
        turns = 0
        possibilities = {-1, 1}
        queue = deque([initial_lock])
        deadends_set = set(deadends)
        visited = set({initial_lock})
        if initial_lock in deadends_set:
            return -1
        while queue:
            for _ in range(len(queue)):
                lock = queue.popleft()
                if lock == target:
                    return turns
                for j, wheel in enumerate(lock):
                    for possibility in possibilities:
                        option = (int(wheel) + possibility) % 10
                        new_lock = lock[:j] + str(option) + lock[j+1:]
                        if new_lock not in visited and new_lock not in deadends_set:
                            queue.append(new_lock)
                            visited.add(new_lock)
            turns += 1
        return -1