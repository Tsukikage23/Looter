class Solution(object):
    def peakValleyDifference(self, nums):
        a = 0
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                a+=nums[i]
            elif nums[i-1] > nums[i] < nums[i+1]:
                a-=nums[i]
        return a