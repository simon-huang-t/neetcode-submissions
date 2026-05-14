class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Use Floyd's algorithm to detect cycles:
        1) If there is a cycle not involving 1 --> Not a Happy number(Return False)
        2) If pointers meet at 1 --> Happy number (Return True)
        '''
        
        def next_number(number):
            total = 0
            while number:
                number, digit = divmod(number, 10)
                total += digit * digit
            return total
        
        slow = next_number(n)
        fast = next_number(next_number(n))
        while slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return slow == 1

