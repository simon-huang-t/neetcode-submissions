class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        res = [0] * n
        for i in range(n - 1, - 1, - 1):
            total = digits[i] + carry
            carry, digit = divmod(total, 10)
            res[i] = digit
        if carry:
            res = [carry] + res
            

        return res