class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
            l, r = i + 1, n - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([a, nums[r], nums[l]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res