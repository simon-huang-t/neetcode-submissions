class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i, num in enumerate(nums):
            xorr ^= i ^ num
        return xorr