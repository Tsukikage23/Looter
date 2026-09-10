# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        prev = None
        slow = head
        fast = head
        sum1 = 0
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        prev = None
        while slow:
            a = slow.next
            slow.next = prev
            prev = slow
            slow = a
        while prev:
            sum1 = max(sum1,head.val + prev.val)
            prev = prev.next
            head = head.next
        return sum1