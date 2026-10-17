class Solution(object):
    def alternatingSum(self, nums):
        a = 0
        b = 0
        for i in nums:
            if b == 0:
                a+=i
                b = 1
            else:
                a-=i
                b = 0
        return a