# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        def reverse(node):
            prevNode = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = prevNode
                prevNode = cur
                cur = tmp
            return prevNode
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            kth.next = None
            group_start = group_prev.next
            new_head = reverse(group_start)

            group_prev.next = new_head
            group_start.next = group_next
            group_prev = group_start
        
        