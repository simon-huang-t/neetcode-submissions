class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Slow and fast pointers
        1) 2 steps increment for fast and 1 step increment for slow
        2) If they are equal, and not equal to 1, then return False
        3) If they are equal and equal to 1 then return True (non-cyclical)
        '''
        def sum_squares(number):
            string_number = str(number)
            total = 0
            for c in string_number:
                total += int(c) ** 2
            return total
        slow, fast = sum_squares(n), sum_squares(sum_squares(n))
        while slow != fast:
            slow, fast = sum_squares(slow), sum_squares(sum_squares(fast))
        return True if slow == 1 else False


        