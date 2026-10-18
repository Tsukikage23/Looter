class Solution(object):
    def largestPerimeter(self, nums):
        nums = sorted(nums)[::-1]
        if nums[0] == 0:
            return 0
        for i in range(1,len(nums)-1):
            if nums[i] + nums[i+1] > nums[i-1]:
                return nums[i] + nums[i+1] + nums[i-1]
        return 0