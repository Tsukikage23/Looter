class Solution(object):
    def findPermutationDifference(self, s, t):
        a = 0
        for i,n in enumerate(s):
            b = t.index(n)
            a += abs(b-i)
        return a