# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, LINKEDLIST: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, LINKEDLIST

        while current: # this is checking if the value is truthy
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous # we return this because after reversing the LL the previous value
        # is acutually the new "head" persay
