class Solution(object):
    def absDifference(self, nums, k):
        a = 0
        nums.sort()
        for i in range(k):
            a -= nums[i]
            a += nums[len(nums)-i-1]
        return a