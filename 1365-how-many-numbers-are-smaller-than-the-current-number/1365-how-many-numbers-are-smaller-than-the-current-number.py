class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a = [0]*101
        for i in nums:
            a[i]+=1
        b = list()
        for i in range(len(nums)):
            c = sum(a[:nums[i]])
            b.append(c)
        return b