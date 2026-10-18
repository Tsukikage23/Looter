class Solution(object):
    def maximizeSum(self, nums, k):
        a = max(nums)
        m = a * k + ((k-1)*k/2)
        return m
