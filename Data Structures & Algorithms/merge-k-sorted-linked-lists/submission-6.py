# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ListNode.__lt__ = lambda self, other: self.val < other.val
        dummy = ListNode()
        tail = dummy
        heap = []
        counter = 0
        for l in lists:
            if l:
                counter += 1
                heapq.heappush(heap, (l.val, counter, l))
                
        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                counter += 1
                heapq.heappush(heap, (node.next.val, counter, node.next))
        return dummy.next