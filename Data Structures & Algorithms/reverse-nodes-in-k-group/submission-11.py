# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        1) Find kth
        2) Detach
        3) Reverse
        4) Attach
        5) Advance
        group_prev | group_start kth | group_next
        group_prev | new_head group_start | group_next
        '''
        def reverse(node):
            prevNode = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = prevNode
                prevNode = cur
                cur = tmp 
            return prevNode
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
        
            group_next = kth.next
            group_start = group_prev.next
            kth.next = None
            new_head = reverse(group_start)

            group_start.next = group_next
            group_prev.next = new_head
            group_prev = group_start
