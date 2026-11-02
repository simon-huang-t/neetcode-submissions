class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # min_value = float('inf')
        for i in range(n - 1):
            min_value = nums[i]
            swap_index = i
            for j in range(i + 1, n):
                if nums[j] < min_value:
                    min_value = nums[j]
                    swap_index = j
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
        return nums
