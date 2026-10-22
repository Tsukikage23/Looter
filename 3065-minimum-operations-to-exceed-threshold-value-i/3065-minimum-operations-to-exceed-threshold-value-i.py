class Solution(object):
    def minOperations(self, nums, k):
        a = 0
        return sum(1 for i in nums if i < k)