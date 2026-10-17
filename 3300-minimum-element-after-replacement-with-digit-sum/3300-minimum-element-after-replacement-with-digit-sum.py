class Solution(object):
    def minElement(self, nums):
        b = list()
        for i in nums:
            a = 0
            while i > 0:
                a += i%10
                i//=10
            b.append(a)
        return min(b)