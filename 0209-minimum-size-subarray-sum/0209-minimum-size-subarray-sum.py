class Solution(object):
    def minSubArrayLen(self, target, nums):
        sum1 = 0
        left = 0
        count = 0
        finalcount = 1000000
        for right in range(len(nums)):
            sum1 += nums[right]
            while sum1 >= target:
                finalcount = min(right -left +1,finalcount)
                sum1 -= nums[left]
                left+=1
        if finalcount == 1000000:
            return 0
        return finalcount