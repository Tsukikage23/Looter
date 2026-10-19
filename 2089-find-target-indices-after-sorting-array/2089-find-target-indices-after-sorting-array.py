class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        a = list()
        for i in range(len(nums)):
            if nums[i] == target:
                a.append(i)
        return a