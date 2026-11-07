'''
[0, 2, 1, 2, 4]
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        # seen = {0: 1} # (value: freq)
        seen = defaultdict(int)
        seen[0] = 1
        count = 0
        for i, num in enumerate(nums):
            prefix += num
            value = prefix - k
            if value in seen:
                count += seen[value]
            seen[prefix] += 1
        return count


        # n = len(nums)
        # prefix = [0] * (n + 1)
        # for i, num in enumerate(nums):
        #     prefix[i + 1] = num + prefix[i]
        # # seen = {0: 1} # (value: freq)
        # seen = defaultdict(int)
        # seen[0] = 1
        # count = 0
        # for i in range(1, n + 1):
        #     value = prefix[i] - k
        #     if value in seen:
        #         count += seen[value]
        #     seen[prefix[i]] += 1
        # return count

