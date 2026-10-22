class Solution(object):
    def createTargetArray(self, nums, index):
        a = list()
        for i in range(len(nums)):
            a.insert(index[i],nums[i])
        return a