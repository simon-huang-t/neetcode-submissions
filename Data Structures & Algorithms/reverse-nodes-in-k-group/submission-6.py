# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        prev_group | group_start  ... kth | group_next
        prev_group | new_head  ... group_start | group_next

        1) Find kth node
        2) Cut
        3) Reverse current group
        4) Attach
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
        prev_group = dummy
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_start = prev_group.next
            group_next = kth.next
            kth.next = None
            new_head = reverse(group_start)
            group_start.next = group_next
            prev_group.next = new_head
            prev_group = group_start