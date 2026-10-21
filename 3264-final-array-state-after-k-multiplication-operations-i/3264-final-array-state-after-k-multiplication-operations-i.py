class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        while k > 0:
            a = min(nums)
            b = nums.index(a)
            nums[b] = a*multiplier
            k-=1
        return nums