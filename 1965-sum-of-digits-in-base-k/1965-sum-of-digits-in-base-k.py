class Solution(object):
    def sumBase(self, n, k):
        sum1 = 0
        while n > 0:
            sum1 += n%k
            n//=k
        return sum1