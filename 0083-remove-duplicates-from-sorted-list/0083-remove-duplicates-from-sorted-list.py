# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        a = head
        if not a or not a.next:
            return a
        while a and a.next:
            if a.val == a.next.val:
                a.next = a.next.next
            else:
                a = a.next
        return head