'''
25/08/26 (2 months after the latest one)
3min30
A few hesitations but one-shot
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        dummy = ListNode()
        tail = dummy
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)
        while heap:
            node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, node.next)
        return dummy.next