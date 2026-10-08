class Solution(object):
    def pivotInteger(self, n):
        a = sum(range(n+1))
        b = 0
        for i in range(1,n+1):
            b += i
            if b == a:
                return i
            a -= i
        return -1