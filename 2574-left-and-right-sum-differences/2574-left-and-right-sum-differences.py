class Solution(object):
    def leftRightDifference(self, nums):
        a = [0]*len(nums)
        b = [0]*len(nums)
        for i in range(1,len(nums)):
            a[i] = nums[i-1] + a[i-1]
        for i in range(len(nums)-2,-1,-1):
            b[i] = nums[i+1] + b[i+1]
        for i in range(len(nums)):
            a[i] = abs(a[i]-b[i])
        return a