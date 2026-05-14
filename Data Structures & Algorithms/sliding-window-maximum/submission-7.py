class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = 0
        res = []
        for r, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(r)

            while queue and queue[0] <= r - k :
                queue.popleft()

            if r >= k - 1:
                res.append(nums[queue[0]])
        return res
