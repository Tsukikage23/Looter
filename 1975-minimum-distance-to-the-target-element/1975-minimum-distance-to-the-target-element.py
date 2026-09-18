class Solution(object):
    def getMinDistance(self, nums, target, start):
        a = 999999
        for i in range(len(nums)):
            if nums[i] == target:
                a = min(a,abs(start - i))
        return a