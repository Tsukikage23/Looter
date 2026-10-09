class Solution(object):
    def differenceOfSum(self, nums):
        a = 0
        for i in nums:
            a+=i
            while i > 0:
                a -= i%10
                i//=10
        return a