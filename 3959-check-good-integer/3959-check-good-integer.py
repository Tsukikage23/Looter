class Solution(object):
    def checkGoodInteger(self, n):
        a = 0
        while n > 0:
            b = n%10
            a += b**2
            a -= b
            n//=10
        return a >= 50