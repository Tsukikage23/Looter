class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        min1 = 99999
        a = nums[0] - min(nums)
        if a <= k:
            min1 = 0
        for i in range(1,n):
            score = max(nums[0:i+1]) - min(nums[i:n])
            if score <= k:
                min1 = min(min1,i)
        if min1 == 99999:
            return -1
        return min1