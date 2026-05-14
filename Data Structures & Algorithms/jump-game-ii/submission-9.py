class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        further = 0
        currentEnd = 0
        for i in range(len(nums) - 1):
            further = max(further, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = further

        return jumps