# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        dummy = ListNode(0, head)
        prev = dummy
        # while cur:
        while True:
            cur = prev
            for _ in range(k):
                cur = cur.next
                if not cur:
                    return dummy.next
                
            next = cur.next
            cur.next = None
            group_start = prev.next
            new_head = reverse(group_start)

            prev.next = new_head
            group_start.next = next
            prev = group_start
            
            # tail.next = next
            # prev.next = cur
            # prev = tail
            # tail = next
        return dummy.next