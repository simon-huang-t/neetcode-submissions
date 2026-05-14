class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i, num in enumerate(nums):
            res[i] *= prefix
            prefix *= num
        suffix = 1
        for i in range(n - 1, - 1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        postfix = 1
        return res