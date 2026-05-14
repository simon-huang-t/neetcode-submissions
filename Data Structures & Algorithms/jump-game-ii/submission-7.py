class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current_end = 0
        n = len(nums)
        jumps = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps