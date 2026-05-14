class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            cur = nums[mid]
            if cur <= nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
