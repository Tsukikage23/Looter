# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        a = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        if head.next is None:
            return head
        while curr:
            if curr.val in a:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next