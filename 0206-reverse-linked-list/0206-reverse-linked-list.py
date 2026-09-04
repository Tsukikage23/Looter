# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev = None
        a = head
        while a:
            b = a.next
            a.next = prev
            prev = a
            a = b
        return prev