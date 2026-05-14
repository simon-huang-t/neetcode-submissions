# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1) Find middle
        2) Reverse second half
        3) Merge both

        1->None
        1->2->None

        1->2->3->None
        1->2->3->4->None
        '''
        dummy = ListNode(0, head) #
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None #cut

        def reverse(node):
            cur = node
            prevNode = None
            while cur:
                tmp = cur.next
                cur.next = prevNode
                prevNode = cur
                cur = tmp
            return prevNode
        
        second = reverse(second)
        first = dummy.next
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        # return dummy.next














        

