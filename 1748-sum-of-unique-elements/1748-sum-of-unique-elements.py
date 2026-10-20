class Solution(object):
    def sumOfUnique(self, nums):
        b = 0
        for i in range(len(nums)-1):
            if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
                b+=nums[i]
        if nums[-1] not in nums[:-1]:
            b+=nums[-1]
        return b