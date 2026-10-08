class Solution(object):
    def findDuplicates(self, nums):
        a = list()
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                a.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        return a