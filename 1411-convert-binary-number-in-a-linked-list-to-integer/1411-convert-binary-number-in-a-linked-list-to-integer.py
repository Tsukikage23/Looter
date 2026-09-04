# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        n = 0
        a = head
        num = 0
        while a:
            n+=1
            a=a.next
        a = head
        n-=1
        while a:
            num+=(2**n)*a.val
            n-=1
            a = a.next
        return num