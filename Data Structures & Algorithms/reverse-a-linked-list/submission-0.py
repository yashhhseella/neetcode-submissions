# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            temp = curr.next # next node to move to
            curr.next = prev # setting node we are on to point to node behind it
            prev = curr
            curr = temp
        
        return prev
        