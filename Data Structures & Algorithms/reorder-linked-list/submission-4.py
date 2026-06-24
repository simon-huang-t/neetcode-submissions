# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    '''
    0->1->None
    m
    s  f
    0->1->2->None
        m
    s  f
        s     f      
    '''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1) Find middle
        2) Cut
        3) Reverse
        4) Merge
        '''
        def reverse(node):
            cur = node
            prevNode = None
            while cur:
                tmp = cur.next
                cur.next= prevNode
                prevNode = cur
                cur = tmp
            return prevNode

        def find_middle(node):
            slow, fast = node, node #
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        dummy = ListNode(0, head)
        tail = dummy

        middle = find_middle(tail)
        group_next = middle.next
        middle.next = None
        second = reverse(group_next)
        first = head
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            




