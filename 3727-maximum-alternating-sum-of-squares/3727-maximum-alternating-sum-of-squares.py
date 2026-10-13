class Solution(object):
    def maxAlternatingSum(self, nums):
        a = sorted(x*x for x in nums)
        n = len(a)
        c = n//2
        return sum(a[c:]) - sum(a[:c])