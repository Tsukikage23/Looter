# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        a = slow.next
        slow.next = None
        prev = None
        while a:
            b = a.next
            a.next = prev
            prev = a
            a = b
        c = head
        while prev:
            d = c.next
            e = prev.next
            c.next = prev
            prev.next = d
            c = d
            prev = e
        return head