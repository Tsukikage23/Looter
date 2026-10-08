class Solution(object):
    def isBalanced(self, num):
        a = 0
        b = 0
        for i in num:
            if b == 0:
                a += int(i)
                b = 1
            else:
                a -= int(i)
                b = 0
        return a == 0