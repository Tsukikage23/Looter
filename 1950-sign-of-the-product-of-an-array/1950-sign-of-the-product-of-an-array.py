class Solution(object):
    def arraySign(self, nums):
        a = 0
        for i in nums:
            if i < 0:
                a+=1
            elif i == 0:
                return 0
        if a % 2 == 0:
            return 1
        return -1