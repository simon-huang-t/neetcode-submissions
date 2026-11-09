class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]
        n = len(nums)
        for num in nums:
            if num != candidate:
                count -= 1
                if count == 0:
                    candidate = num
                    count = 1
            else:
                count += 1
        return candidate