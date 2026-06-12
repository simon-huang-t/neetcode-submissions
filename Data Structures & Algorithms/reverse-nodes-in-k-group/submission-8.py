# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        1. Find kth node
        2. Reverse group
        3. Cut
        4. Attach
        5. Advance
        prev |group_start kth| group_next
        prev |new_head group_start| group_next
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
        prev = dummy
        while True:
            kth = prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            kth.next = None
            group_start = prev.next
            new_head = reverse(group_start)

            group_start.next = group_next
            prev.next = new_head
            prev = group_start




