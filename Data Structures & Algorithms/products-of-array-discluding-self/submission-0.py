class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        n = len(nums)
        res = [1] * n
        for i, num in enumerate(nums):
            res[i] = prefix
            prefix *= num
        postfix = 1
        for i in range(n - 1, - 1, - 1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
            