class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1 or 0 not in nums:
            return True
        maxreach = 0
        for i in range(len(nums)):
            if maxreach < i:
                return False
            a = i + nums[i]
            maxreach = max(a,maxreach)
        return True