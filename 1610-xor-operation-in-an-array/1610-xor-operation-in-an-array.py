class Solution(object):
    def xorOperation(self, n, start):
        b = 0
        for i in range(n):
            b^=start+2*i
        return b