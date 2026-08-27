# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)
        dummy = ListNode()
        tail = dummy
        while heap:
            node = heapq.heappop(heap)
            tail.next = node
            if node.next:
                heapq.heappush(heap, node.next)
            tail = tail.next
        return dummy.next