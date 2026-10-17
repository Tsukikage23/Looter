class Solution(object):
    def maxProduct(self, n):
        s = list(str(n))
        s.sort()
        return int(s[-1])*int(s[-2])