# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        group_prev | group_start kth | group_next
        group_prev | new_start group_start | group_next
        1. Find kth
        2. Detach
        3. Reverse
        4. Attach
        5. Advance
        '''
        def reverse(node):
            cur = node
            prevNode = None
            while cur:
                tmp = cur.next
                cur.next = prevNode
                prevNode = cur
                cur = tmp
            return prevNode
        dummy = ListNode(0, head) #
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            kth.next = None
            group_start = group_prev.next
            new_start = reverse(group_start)

            group_start.next = group_next
            group_prev.next = new_start
            # group_prev = kth
            group_prev = group_start


            

