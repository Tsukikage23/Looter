class Solution(object):
    def numOfPairs(self, nums, target):
        a = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        a+=1
        return a