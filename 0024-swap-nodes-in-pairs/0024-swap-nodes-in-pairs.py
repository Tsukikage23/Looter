class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            first = curr.next
            age = curr.next.next
            ageval = age.next

            curr.next = age
            age.next = first
            first.next = ageval
            curr = first
        return dummy.next