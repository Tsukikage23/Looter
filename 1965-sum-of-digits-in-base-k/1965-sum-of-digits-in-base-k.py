class Solution(object):
    def sumBase(self, n, k):
        a = []
        while n > 0:
            b = n%k
            a.append(b)
            n//=k
        return sum(a)