class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0:
            return True
        a = num%10
        return a != 0