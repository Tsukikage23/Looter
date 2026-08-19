class Solution(object):
    def moveZeroes(self, nums):
        zero = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero+=1
            else:
                nums[k] = nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i] = 0
        return nums