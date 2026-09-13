class Solution(object):
    def findGCD(self, nums):
        mina = min(nums)
        maxa = max(nums)
        b = 0
        for i in range(1,mina+1):
            if maxa%i == 0 and mina%i == 0:
                b = i
        return b