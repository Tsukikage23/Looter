class Solution(object):
    def maxAdjacentDistance(self, nums):
        a = 0
        for i in range(len(nums)-1):
            b = abs(nums[i] - nums[i+1])
            a = max(a,b)
        c = abs(nums[-1] - nums[0])
        a = max(a,c)
        return a