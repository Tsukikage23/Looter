class Solution(object):
    def minMoves(self, nums):
        a = max(nums)
        b = 0
        for i in nums:
            b += a - i
        return b