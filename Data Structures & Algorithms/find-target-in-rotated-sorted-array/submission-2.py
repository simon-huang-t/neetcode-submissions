class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            cur = nums[mid]
            if cur == target:
                return mid
            elif cur >= nums[l]: #left sorted
                if nums[l] <= target < cur:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if cur < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return - 1