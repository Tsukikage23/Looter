class Solution(object):
    def maxSubArray(self, nums):
        maxsum = nums[0]
        sum1 = 0
        if len(nums) == 1:
            return maxsum
        
        for i in nums:
            sum1+=i
            maxsum = max(sum1,maxsum)
            if sum1<0:
                sum1 = 0
                continue
        return maxsum        