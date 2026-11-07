class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_size = float('inf')
        l = 0
        cur_sum = 0
        for r, num in enumerate(nums):
            cur_sum += num
            while l < n and cur_sum >= target: 
                min_size = min(min_size, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            
        return min_size if min_size != float('inf') else 0