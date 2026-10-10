class Solution(object):
    def minOperations(self, nums):
        a = 0
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                b = nums[i+1]
                nums[i+1] = nums[i]+1
                a+= nums[i+1] - b
        return a