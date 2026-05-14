# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Why dummy node?
# dummy
# head -> None


# head->1->None
# head->None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2 approaches:
        1) Iterate though both linked list at the same time. Then add them one by one.
        2) Iterathe through both linked list separately and get the numbers. Then add them.
        '''
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            current_sum = l1val + l2val + carry
            # carry = current_sum // 10
            # digit = current_sum % 10
            carry, digit = divmod(current_sum, 10)
            node = ListNode(digit)
            cur.next = node
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

