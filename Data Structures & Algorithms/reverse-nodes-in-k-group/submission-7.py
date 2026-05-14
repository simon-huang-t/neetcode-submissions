# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        group_prev | group_start ... kth | group_next
        group_prev | new_head ... group_start | group_next
        1) Find kth node
        2) Reverse
        3) Cut
        4) Reattach
        5) Advance
        '''
        def reverse(node):
            cur = node
            prev = None
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_start = group_prev.next
            group_next = kth.next
            kth.next = None
            new_head = reverse(group_start)
            group_start.next = group_next
            group_prev.next = new_head
            group_prev = group_start