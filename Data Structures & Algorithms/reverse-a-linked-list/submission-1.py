# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None # None is equivalent to null in Python

        newHead = head
        if head.next: # if head.next is not null
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

# Time: O(n), Space: O(n)

#  reverseList(1)
#     reverseList(2)
#         reverseList(3)
#             return 3

#         3.next = 2
#         2.next = None
#         return 3

#     2.next = 1
#     1.next = None
#     return 3       