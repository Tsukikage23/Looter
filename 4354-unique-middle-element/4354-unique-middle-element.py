class Solution(object):
    def isMiddleElementUnique(self, nums):
        n = len(nums)-1
        a = nums[n/2]
        count = 0
        if len(nums) == 1:
            return True
        for i in nums:
            if i == a:
                count+=1
            if count > 1:
                return False
        return True