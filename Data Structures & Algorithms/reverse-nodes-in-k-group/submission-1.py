# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            cur = node
            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1️⃣ Find kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # not enough nodes

            group_next = kth.next

            # 2️⃣ قطع the group
            kth.next = None
            group_start = group_prev.next

            # 3️⃣ reverse the group
            new_head = reverse(group_start)

            # 4️⃣ reconnect
            group_prev.next = new_head
            group_start.next = group_next

            # 5️⃣ move to next group
            group_prev = group_start